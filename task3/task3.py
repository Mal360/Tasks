# Программа, которая формирует файл report.json с заполненными полями value для структуры tests.json на основании values.json
import json


def task3(path_values, path_tests, path_report):
    def change_values(values, tests):
        for test in tests:
            if "values" in test:
                change_values(values, test["values"])
            if "value" in test:
                for i, value in enumerate(values):
                    if test["id"] == value["id"]:
                        test["value"] = value["value"]
                        del values[i]
                        break
            else:
                continue

    with open(path_values, "r") as file_values:
        data_values = json.load(file_values)

    with open(path_tests, "r") as file_tests:
        data_tests = json.load(file_tests)

    change_values(data_values["values"], data_tests["tests"])

    with open(path_report, "w") as file_report:
        json.dump(data_tests, file_report, indent=2)


if __name__ == "__main__":
    task3("values.json", "tests.json", "report.json")
