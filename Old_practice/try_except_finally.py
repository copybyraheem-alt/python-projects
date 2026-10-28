def calculate_average(values):
    total = 0
    count = 0

    for value in values:
        try:
            val = float(value)
            total += val
            count += 1
        except ValueError:
            print(f"Skipping invalid value: {value}")
        except TypeError:
            print(f"Skipping wrong type: {value}")
        finally:
            print(f"Processed: count= {count}, Current value= {value}")
            print("----------------------------------------------------")

    if count == 0:
        print("No valid values to average")
        return 0.0
    else:
        average = total / count
        return average


if __name__ == "__main__":
    print(calculate_average([10, "20", 30, "hello", None, "40"]))
    print("---------NEW ROUND---------------")
    print(calculate_average(["a", "b", None]))
