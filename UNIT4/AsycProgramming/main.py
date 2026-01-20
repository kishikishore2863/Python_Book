import asyncio



# This creates an event loop and indefinitely cycles through
# its collection of jobs.



def hello_printer():
    print(
        "Hi, I am a lowly, simple printer, though I have all I "
        "need in life -- \nfresh paper and my dearly beloved octopus "
        "partner in crime."
    )
hello_printer()

async def loudmouth_penguin(magic_number: int):
        print(
         "I am a super special talking penguin. Far cooler than that printer. "
         f"By the way, my lucky number is: {magic_number}."
        )
asyncio.run(loudmouth_penguin(3))
print(loudmouth_penguin(3))
