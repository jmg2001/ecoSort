import streamlit as st
from camera_input_live import camera_input_live

st.write("# See a new image every second")
controls = st.checkbox("Show controls")
image = camera_input_live(show_controls=controls)
if image is not None:
    st.image(image)

def camera_input_live(
    debounce: int = 10,
    height: int = 530,
    width: int = 704,
    key: Optional[str] = None,
    show_controls: bool = True,
    start_label: str = "Start capturing",
    stop_label: str = "Pause capturing",
) -> Optional[BytesIO]:
    """
    Add a descriptive docstring
    """
    b64_data: Optional[str] = _component_func(
        height=height,
        width=width,
        debounce=debounce,
        showControls=show_controls,
        startLabel=start_label,
        stopLabel=stop_label,
        key=key,
    )

    if b64_data is None:
        return None

    raw_data = b64_data.split(",")[1]  # Strip the data: type prefix

    component_value = BytesIO(base64.b64decode(raw_data))

    return component_value