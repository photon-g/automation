
import os

current_ref = os.environ["CBRANCH"]
token = os.environ["GITHUB_TOKEN"]
git_repo = os.environ["GITHUB_REPOSITORY"]

#curl method
api_method=f"https://api.github.com/repos/{git_repo}/git/{current_ref}"
h_op_1="Accept: application/vnd.github+json"
h_op_2=f"Authorization: Bearer {token}"
h_op_3="X-GitHub-Api-Version: 2022-11-28"

l_curl_cmd=f'curl -L -X DELETE -H "{h_op_1}" -H "{h_op_2}" -H "{h_op_3}"'+" "+api_method 
print(l_curl_cmd)
os.system(l_curl_cmd)
