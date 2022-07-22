import lightning as L
from lightning.app.frontend import StreamlitFrontend

def render_streamlit(app_state):
    import os
    os.system("pip uninstall opencv-python && pip install opencv-python-headless")
    import app

class LitApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
    
    def configure_layout(self):
        return StreamlitFrontend(render_fn=render_streamlit)


app = L.LightningApp(LitApp())
