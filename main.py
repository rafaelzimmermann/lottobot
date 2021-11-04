import asyncio
import random
import sys
import yaml

from messenger import Telegram


async def async_main(config):
    telegram = Telegram(config['telegram']['token'])
    timer = asyncio.get_event_loop().time

    def print_sena(chat_id: int):
        numbers = []
        r = random.Random()
        while len(numbers) < 6:
            n = r.randint(1, 60)
            if n not in numbers:
                numbers.append(n)

        message = f"Numbers: {sorted(numbers)}"
        telegram.send(chat_id, message)

    def print_numbers(chat_id: int):
        numbers = []
        r = random.Random()
        while len(numbers) < 6:
            n = r.randint(1, 49)
            if n not in numbers:
                numbers.append(n)

        message = f"Numbers: {sorted(numbers)}, Superzahl: {r.randint(0, 9)}"
        telegram.send(chat_id, message)

    def print_updates():
        for u in telegram.updates:
            message = u['message']
            if '/lotto' in message['text']:
                print_numbers(message['chat']['id'])
            if '/sena' in message['text']:
                print_sena(message['chat']['id'])

    interval = 10  # seconds

    while True:
        await asyncio.sleep(interval - timer() % interval)
        print_updates()


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as _f:
        asyncio.run(async_main(yaml.safe_load(_f)))



