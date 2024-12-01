#!/bin/bash

# Function to initialize the session
initialize_session() {
  curl -s -X GET http://13.61.152.55:8080/init
}

# Function to fetch the math problem
fetch_problem() {
  curl -s -X GET http://13.61.152.55:8080/
}

# Function to submit the solution
submit_answer() {
  local answer=$1
  curl -s -X POST http://13.61.152.55:8080 \
    -H "Content-Type: application/json" \
    --data "{\"answer\": $answer}"
}

# Initialize the session
initialize_session

# Main loop to solve problems
while true; do
  # Fetch the problem
  response=$(fetch_problem)

  # Extract relevant data
  problem=$(echo $response | grep -oP '(?<="message":")[^"]*')
  solved=$(echo $response | grep -oP '(?<="solved":)[^,]*')

  # Break if all problems are solved
  if [ "$solved" == "true" ]; then
    echo "All problems solved."
    break
  fi

  # Solve the problem using bc
  answer=$(echo "$problem" | bc)

  # Submit the answer
  submit_answer "$answer"
done


