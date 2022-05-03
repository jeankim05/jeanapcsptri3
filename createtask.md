{% include navigation.html %}

**Crossover Comments for Create Task by Isaac Le**
- I like the concept and the purpose of the program calculating
- Video has all the requirements that collegeboard asks for
- Inclides a list that stores the different number inputs for your grade
- Calls back to the list multiple times in order to input different subjects/grades
- Create task is very interesting and can be very useful to people as they can figure out what they need to do in the class in order to achieve the grade that they desire


Create Task Details:
Food Quiz

The Food Quiz page is the practice create task. It's main goal is to quiz users on different foods  as related to countries so that users can remember which countries offer which cullinary dishes and information.

Program Purpose: Create a page that quizzes users based on different foods and countries

Input: Selecting answers for questions

Output: Displays user score upon submission

Lists: Stores questions and answers in a list, then displays them later.

Procedure: Once the user fills out all of the questions, the website will add +1 to the user's score if the answer is correct, then display it.

Parameters: Score after user submits quiz

Sequencing: User input in the quiz, Adds to score in case of a correct answer, Return name of restaurants that fit

Selection: Adds to score in case of a correct answer

Iteration: Program loops for every question

Code Snippets:

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
