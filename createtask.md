{% include navigation.html %}

Create Task Details:
Sports Quiz

The sports Quiz page is the practice create task. It's main goal is to quiz users on different sports as related to countries so that users can remember which countries offer which sports and information.

This page will be integrated into our website as a PBL feature for now. The users will see a page where they can answer multiple-choice questions and receive their score upon submitting the quiz.

Program Purpose: Create a page that quizzes users based on different foods and countries

Input: Selecting answers for questions

Output: Displays user score upon submission

Lists: Stores questions and answers in a list, then displays them later.

Procedure: Once the user fills out all of the questions, the website will add +1 to the user's score if the answer is correct, then display it.

Parameters: Score after user submits quiz

Sequencing: User input in the quiz, Adds to score in case of a correct answer, Return name of restaurants that fit

Selection: Adds to score in case of a correct answer

Iteration: Program loops for every question

Two Code Snippets:

const quizContainer = document.getElementById('quiz'); const resultsContainer = document.getElementById('results'); const submitButton = document.getElementById('submit'); const myQuestions = [ ]

function showResults(){

            const answerContainers = quizContainer.querySelectorAll('.answers');

            let numCorrect = 0;

            myQuestions.forEach( (currentQuestion, questionNumber) => {


                const answerContainer = answerContainers[questionNumber];
                const selector = `input[name=question${questionNumber}]:checked`;
                const userAnswer = (answerContainer.querySelector(selector) || {}).value;

                if(userAnswer === currentQuestion.correctAnswer){

                    numCorrect++;


                    answerContainers[questionNumber].style.color = 'darkgreen';
                }

                else{

                    answerContainers[questionNumber].style.color = 'red';
                }
            });
