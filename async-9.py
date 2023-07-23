# example of  an asynchronous itertor with async for loop
import asyncio
import time

#define an asynchronous iterator 
class AnyncItertor():
    #costructor, degine some state
    def __init__(self):
        self.counter = 0 

    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return the next awaitable
    async def __anext__(self):
        #check for no furture items
        if self.counter > 10:
            raise StopAsyncIteration
        #increment the counter
        self.counter += 1
        #simulate woek
        await asyncio.sleep(1)
        #return the counter value
        return self.counter
    
#main coroutine
async def main():
    #loop over async iterator with async for loop
    async for item in AnyncItertor():
        print(f'{time.ctime()} {item}')
#execute the  astncio program
asyncio.run(main())


# Wed Jul 19 14:56:05 2023 1
# Wed Jul 19 14:56:06 2023 2
# Wed Jul 19 14:56:07 2023 3
# Wed Jul 19 14:56:08 2023 4
# Wed Jul 19 14:56:09 2023 5
# Wed Jul 19 14:56:11 2023 6
# Wed Jul 19 14:56:12 2023 7
# Wed Jul 19 14:56:13 2023 8
# Wed Jul 19 14:56:14 2023 9
# Wed Jul 19 14:56:15 2023 10
# Wed Jul 19 14:56:16 2023 11