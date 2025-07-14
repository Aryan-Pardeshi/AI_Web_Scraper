import streamlit as st

from scrape import scrape_website, split_dom_content, clean_body_content, extract_body
from parse import parse_with_Gemini

st.title("AI Web Scraper")
url = st.text_input("Enter the URL to scrape: \n(Include https://)")

if st.button("Scrape Site"):
    st.write(f"Scraping the site: {url}")
    result = scrape_website(url)
    # print(result)  # Display the scraped HTML in the console
    
    body_content = extract_body(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content # Store the cleaned content in session state so that we can give it to the AI model later
    
    with st.expander("View Scraped Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
if "dom_content" in st.session_state:
    parse_discription = st.text_area("Describe what u want to parse?")
    
    if st.button("Parse Content"):
        if parse_discription:
            st.write("Parsing content based on your description...")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_Gemini(dom_chunks, parse_discription)
            st.write(result)
            
            with open("parsed_result.txt", "w") as f:
                f.write(result)
                st.success("Parsed results saved to parsed_result.txt")
                
            

