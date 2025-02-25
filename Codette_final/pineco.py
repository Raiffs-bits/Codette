from pinecone import Pinecone
pc = Pinecone(api_key="pcsk_6vNMvt_Nzk1jwwRPSHSjNj7jsNxLgEuJG63KfXw1nJX9oRPUcsEJTGVpeCgeVXBgoUSHEs")

assistant = pc.assistant.Assistant(
    assistant_name="codette", 
)

response = assistant.upload_file(
    file_path="/Users/jdoe/Downloads/example_file.txt",
    timeout=None
)