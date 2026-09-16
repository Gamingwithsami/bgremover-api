from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove

app = FastAPI()

# ✅ Only allow your Blogger site
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bgremoveron.blogspot.com"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"ok": True, "msg": "BG Remover API is running. Use POST /remove"}

@app.post("/remove")
async def remove_bg(image_file: UploadFile = File(...)):
    data = await image_file.read()
    out = remove(data)  # returns PNG bytes with transparency
    return Response(content=out, media_type="image/png")
