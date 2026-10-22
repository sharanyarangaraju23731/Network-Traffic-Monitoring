import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Network Traffic Monitor",
    layout="wide"
)

st.title("Network Traffic Monitoring")
st.subheader("Real-Time Anomaly Detection Simulator")

@st.fragment(run_every=2)
def show_dashboard():
    if os.path.exists("traffic_log.jsonl") and os.path.getsize("traffic_log.jsonl") > 0:
        df = pd.read_json("traffic_log.jsonl", lines=True)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", len(df))
        col2.metric("Total Packets", int(df["packets_per_second"].sum()))
        col3.metric("Anomalies", int((df["status"] == "Anomaly").sum()))

        st.subheader("Protocol Distribution")
        st.bar_chart(df["protocol"].value_counts())

        st.subheader("Traffic by Source IP")
        traffic = df.groupby("source_ip")["packets_per_second"].sum()
        st.bar_chart(traffic)

        st.subheader("Detected Anomalies")
        anomalies = df[df["status"] == "Anomaly"]

        if len(anomalies) > 0:
            st.warning("Unusual traffic detected!")
            st.dataframe(anomalies, use_container_width=True)
        else:
            st.success("No anomalies detected.")

        st.subheader("Complete Traffic Log")
        st.dataframe(df, use_container_width=True)

        st.download_button(
            "Download Traffic CSV",
            df.to_csv(index=False),
            "traffic_log.csv",
            "text/csv"
        )
    else:
        st.info("No traffic received yet. Start the server and client first.")

show_dashboard()
