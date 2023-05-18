from rules.variable import gitlab
import json

def main():
    variables = gitlab()
    return_json = variables.get_variables()
    for i in return_json:
        variables.post_variables(i)
    #f = open('data.json')
    #data = json.load(f)


if __name__ == "__main__":
    main()