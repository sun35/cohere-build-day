from web import scrape

def main():
    scrape(["https://docs.aws.amazon.com/athena/latest/ug/what-is.html"])
    #response = query("Tell me all about intelligent datadog for tests")
    #print(response)

if __name__ == "__main__":
    main()