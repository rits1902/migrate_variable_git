import requests

class gitlab:

    def __init__(self):
        self.gitlab_old = "xxxxxx"
        self.gitlab_new = "xxxxxx"
        self.headers_old = {'PRIVATE-TOKEN': "xxxxxxxxx"}
        self.headers_new = {'PRIVATE-TOKEN': "xxxxxxxxx"}


    def get_variables(self):
        try:
            r = requests.get(
                self.gitlab_old, 
                headers=self.headers_old
                )
            return r
        except Exception as e:
            print(e)

    def post_variables(self, data):
        if "key" in data:
            form_data = {
                "key": data["key"],
                "value": data['value']
                }
            try:
                r = requests.post(
                    self.gitlab_new, 
                    headers=self.headers_new,
                    data=form_data
                    )
                return r
            except Exception as e:
                print(e)