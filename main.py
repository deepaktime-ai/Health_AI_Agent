from agent import Agent
agent = Agent()
while True:
    user_input=input("\nYou:")
    if user_input.lower() in ["exist","quit"]:
        print("Good Bye")
        break
    response=agent.run(user_input)
    print("\n Health Expert \n",response)

