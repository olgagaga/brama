"""Render Brama mascot concepts with the Gemini image API.

Usage: python3 generate.py [concept ...] [--n N]
Needs GEMINI_API_KEY; optional GEMINI_IMAGE_MODEL. No third-party deps.
"""
import argparse
import base64
import json
import os
import pathlib
import sys
import urllib.request

STYLE = (
    "Soft plush felt 3D character, slightly fuzzy texture, rounded heavy body with a low "
    "centre of gravity, calm friendly eyes (not manic), small confident smile. Studio "
    "lighting, soft shadow, warm off-white seamless background, single muted brand accent "
    "colour (deep teal), no text, no logo, centred full-body, square format. Mood: steady, "
    "reassuring, on your side - a companion, not a toy."
)

CONCEPTS = {
    "zubr": "A plush baby European bison (zubr) calf, round and woolly, no horns, chocolate-brown "
            "fur, sitting solidly on the ground, wearing a tiny teal scarf.",
    "gate": "A non-identifiable plush creature whose body is shaped like a rounded arch or "
            "doorway, two stubby legs, a face on the top of the arch, teal with cream accents.",
    "stork": "A soft round white stork chick with a short orange beak and black wingtips, "
             "standing steadily on two legs, holding a small teal envelope.",
    "butterfly": "A chubby plush butterfly with a round fuzzy body and small soft teal wings, "
                 "sitting rather than flying.",
}


def render(prompt: str, model: str, key: str) -> bytes:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    for part in data["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            return base64.b64decode(part["inlineData"]["data"])
    raise RuntimeError(f"no image in response: {json.dumps(data)[:500]}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("concepts", nargs="*", default=list(CONCEPTS))
    p.add_argument("--n", type=int, default=2)
    args = p.parse_args()

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY is not set")
    model = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
    out = pathlib.Path(__file__).parent / "out"
    out.mkdir(exist_ok=True)

    for name in args.concepts:
        for i in range(1, args.n + 1):
            path = out / f"{name}-{i}.png"
            path.write_bytes(render(f"{CONCEPTS[name]} {STYLE}", model, key))
            print(path)


if __name__ == "__main__":
    main()
