def calculate_average(values):
    Total=0
    count=0

    for value in values:
        try:
            value= float(value)
            Total += value
            count+=1
        except ValueError:
            print(f"Skipping invalid value: {value}")
        except TypeError:
            print(f"Skipping wrong type: {value}")

        finally:
            print(f"Processed: count= {count}, Current value= {value}")
            print("----------------------------------------------------")



    if count ==0:
        print("No valid values to average")
        return 0
    else:
        average= Total/count
        return average
        

print(calculate_average([10, "20", 30, "hello", None, "40"]))
print("---------NEW ROUND---------------")
print(calculate_average(["a", "b", None]))

    

            

