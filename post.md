# Menu Description Writer: An Offline AI Tool for Small Restaurants in Batticaloa

Many small restaurants and tea shops in Batticaloa list only a dish name and price on their menus. Visitors may not know what the food is, and writing good descriptions takes time or money. Cloud AI tools also mean sending the shop's menu and prices to a server the owner doesn't control.

I built a simple app to help. Enter a dish name in English and Tamil, add a short note such as “spicy, fresh crab,” and click one button. A local AI model writes a short, appetizing English description in about 20 seconds. It runs on a normal laptop without internet access.

## Why open-source AI mattered

- **Private:** The menu and prices never leave the laptop.
- **Free to run:** There are no API fees, so a small shop could pay a one-time service fee instead of a subscription.
- **Offline:** It works even with weak or unavailable internet.
- **Swappable:** The model is one line of code, so I can try other open models without rebuilding the app.

## Built with

Gemma 3 (4B) running locally through Ollama, plus Python and Streamlit.

## Where it didn't work

I first asked the model to write Tamil descriptions too. The 4B model's Tamil was unreliable: one result for Idli was meaningless text, and another mixed in broken transliteration.

So I changed the design. The owner types the Tamil dish name, and the model writes only the English description, where it is strong. A small model has limits, and designing around them made the product more honest and useful.

## Status

This is a working prototype, tested on dishes like Chettinad Chicken, Idli, and Filter Coffee. I have not yet tested it with a real shop owner.

## What's next

- Upload a CSV to write a whole menu at once.
- Try a larger open model for Tamil.
- Add local Batticaloa dishes such as buffalo curd, prawn fry, and puttu.
