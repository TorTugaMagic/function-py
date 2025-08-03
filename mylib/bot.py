import wikipedia
# import fire
# from mylib.bot import scrape

def scrape(name="Microsoft", length=5):
    result = wikipedia.summary(name, sentences=length)
    return result


#if __name__ == "__main__":
    #fire.Fire(scrape)