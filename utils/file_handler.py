def read_uploaded_file(uploaded_file):
    """
    Reads uploaded .md file and returns content as string.
    """
    if uploaded_file is not None:
        return uploaded_file.read().decode("utf-8")
    return ""