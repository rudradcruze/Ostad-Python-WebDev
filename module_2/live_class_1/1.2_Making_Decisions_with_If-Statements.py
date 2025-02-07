# Check if a student passed or failed
score = 75
passing_score = 70

# This is like saying: "If you got 70 or higher you pass,
# otherwise you need to try again"
if score >= passing_score:
    print("You passed! 🎉")
    print(f"Your score was {score - passing_score} points above passing!")
else:
    print("Try again next time! 📚")
    print(f"You need {passing_score - score} more points to pass")