import streamlit as st
import pandas as pd

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="File Merger", layout="wide")

st.title("📊 DataFuse App")
st.markdown('''
    __This smart data merging tool is built in Python by [TPCM](https://github.com/tpcm411).__

    *Libraries used: `Streamlit`, `Pandas`, and `Openpyxl`*
''')

st.write("Instructions: Upload multiple CSV or Excel files to merge them under the same headers.")

# ==============================
# NORMALIZE FUNCTION
# ==============================
def normalize_columns(columns):
    return (
        columns.str.strip()
               .str.lower()
               .str.replace(r'\s+', '_', regex=True)
    )

# ==============================
# FILE UPLOADER
# ==============================
uploaded_files = st.file_uploader(
    "Upload files (.csv, .xlsx)",
    type=["csv", "xlsx"],
    accept_multiple_files=True
)

# ==============================
# PROCESS BUTTON
# ==============================
if uploaded_files:
    if st.button("🚀 Merge Files"):

        all_dfs = []
        all_columns = set()

        with st.spinner("Processing files..."):

            for file in uploaded_files:
                try:
                    file_name = file.name

                    # ==============================
                    # HANDLE CSV
                    # ==============================
                    if file_name.endswith(".csv"):
                        try:
                            df = pd.read_csv(file, low_memory=False)
                        except:
                            df = pd.read_csv(file, low_memory=False, encoding='latin1')

                        df.columns = normalize_columns(df.columns)
                        df['source_file'] = file_name
                        df['sheet_name'] = "csv"

                        all_columns.update(df.columns)
                        all_dfs.append(df)

                    # ==============================
                    # HANDLE EXCEL
                    # ==============================
                    elif file_name.endswith(".xlsx"):
                        sheets = pd.read_excel(file, sheet_name=None)

                        for sheet_name, df in sheets.items():
                            if df.empty:
                                continue

                            df.columns = normalize_columns(df.columns)
                            df['source_file'] = file_name
                            df['sheet_name'] = sheet_name

                            all_columns.update(df.columns)
                            all_dfs.append(df)

                except Exception as e:
                    st.error(f"Error processing {file_name}: {e}")

        # ==============================
        # SAFETY CHECK
        # ==============================
        if not all_dfs:
            st.error("❌ No valid data found in uploaded files.")
        else:
            st.success("✅ Files processed successfully!")

            # ==============================
            # ALIGN COLUMNS
            # ==============================
            all_columns = sorted(list(all_columns))

            aligned_dfs = [
                df.reindex(columns=all_columns)
                for df in all_dfs
            ]

            # ==============================
            # CONCAT
            # ==============================
            final_df = pd.concat(aligned_dfs, ignore_index=True)

            # ==============================
            # SHOW PREVIEW
            # ==============================
            st.subheader("📄 Preview")
            st.dataframe(final_df.head(100))

            st.write(f"**Total Rows:** {len(final_df)}")
            st.write(f"**Total Columns:** {len(final_df.columns)}")

            # ==============================
            # DOWNLOAD
            # ==============================
            csv_data = final_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download Merged File",
                data=csv_data,
                file_name="merged-output.csv",
                mime="text/csv"
            )