import os
from datetime import datetime

import pandas as pd
import streamlit as st

APP_TITLE = os.getenv("APP_TITLE", "Streamlit Enterprise POC")
APP_ENV = os.getenv("APP_ENV", "local")


def load_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"service": "frontend", "status": "healthy", "requests": 1024},
            {"service": "api", "status": "healthy", "requests": 830},
            {"service": "db-proxy", "status": "healthy", "requests": 221},
        ]
    )


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🚀", layout="wide")
    st.title(APP_TITLE)
    st.caption("POC for GitHub + Cloud Build + Cloud Deploy + Cloud Run")

    col1, col2, col3 = st.columns(3)
    col1.metric("Status", "Running")
    col2.metric("Environment", APP_ENV.upper())
    col3.metric("Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    st.subheader("Service dashboard")
    df = load_data()
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("service")[["requests"]])

    if st.button("Health check"):
        st.success("OK")

    st.code(
        f"APP_TITLE={APP_TITLE}\nAPP_ENV={APP_ENV}\nPORT={os.getenv('PORT', '8080')}",
        language="bash",
    )


if __name__ == "__main__":
    main()
