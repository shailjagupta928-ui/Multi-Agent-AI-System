import streamlit as st

from agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Multi-Agent AI Research System")
st.caption("Search Agent → Reader Agent → Writer Chain → Critic Chain")

# --- Input ---
with st.form("topic_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Latest advancements in solid-state batteries"
    )
    submitted = st.form_submit_button("Run Research Pipeline", use_container_width=True)

# --- Pipeline run ---
if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
        st.stop()

    state = {}

    # Step 1: Search Agent
    with st.status("Step 1/4 — Search Agent finding sources...", expanded=True) as status:
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [
                (
                    "user",
                    f"Find recent, reliable, and detailed information about: {topic}"
                )
            ]
        })
        state["search_results"] = str(search_result)
        status.update(label="Step 1/4 — Search complete ✅", state="complete")

    with st.expander("🔍 Search Results", expanded=False):
        st.text(state["search_results"])

    # Step 2: Reader Agent
    with st.status("Step 2/4 — Reader Agent scraping top resource...", expanded=True) as status:
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [
                (
                    "user",
                    f"""
Based on the following search results about '{topic}',
pick the most relevant URL and scrape it for deeper content.

Search Results:
{state['search_results'][:1000]}
"""
                )
            ]
        })
        state["scraped_content"] = str(reader_result)
        status.update(label="Step 2/4 — Scraping complete ✅", state="complete")

    with st.expander("📄 Scraped Content", expanded=False):
        st.text(state["scraped_content"])

    # Step 3: Writer Chain
    with st.status("Step 3/4 — Writer drafting the report...", expanded=True) as status:
        research_combined = f"""
SEARCH RESULTS:
{state['search_results']}

DETAILED SCRAPED CONTENT:
{state['scraped_content']}
"""
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
        status.update(label="Step 3/4 — Draft complete ✅", state="complete")

    # Step 4: Critic Chain
    with st.status("Step 4/4 — Critic reviewing the report...", expanded=True) as status:
        state["feedback"] = critic_chain.invoke({
            "report": state["report"]
        })
        status.update(label="Step 4/4 — Review complete ✅", state="complete")

    st.success("Pipeline finished!")

    # --- Results ---
    report_text = state["report"] if isinstance(state["report"], str) else str(state["report"])
    feedback_text = state["feedback"] if isinstance(state["feedback"], str) else str(state["feedback"])

    st.divider()
    st.subheader("📝 Final Report")
    st.markdown(report_text)

    st.download_button(
        label="⬇️ Download Report (Markdown)",
        data=report_text,
        file_name=f"{topic.strip().replace(' ', '_')}_report.md",
        mime="text/markdown",
        use_container_width=True
    )

    st.divider()
    st.subheader("🧐 Critic Feedback")
    st.markdown(feedback_text)

    # Persist results in session so they don't vanish on rerun/interaction
    st.session_state["last_state"] = state

elif "last_state" in st.session_state:
    # Show last results if the user reruns the script (e.g. resizes window) without resubmitting
    state = st.session_state["last_state"]
    st.info("Showing results from the last run.")

    report_text = state["report"] if isinstance(state["report"], str) else str(state["report"])
    feedback_text = state["feedback"] if isinstance(state["feedback"], str) else str(state["feedback"])

    st.subheader("📝 Final Report")
    st.markdown(report_text)

    st.download_button(
        label="⬇️ Download Report (Markdown)",
        data=report_text,
        file_name="report.md",
        mime="text/markdown",
        use_container_width=True
    )

    st.subheader("🧐 Critic Feedback")
    st.markdown(feedback_text)