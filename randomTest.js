// document.write('<script src="tools.js"></script>');
// document.write('<script src="https://cdn.jsdelivr.net/npm/jquery@3.4.0/dist/jquery.min.js"></script>');
// document.write('<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full"></script>');

/**
 * @type {string} fileLocation - 文件路径
 */
function getJSON(fileLocation) {
    a = $.ajax({
        url: fileLocation, //json文件位置，文件名
        type: "GET", //请求方式为get
        dataType: "json", //返回数据格式为json
        async: false,
        success: function(data) { //请求成功完成后要执行的方法 
        }
    });
    result = $.parseJSON(a["responseText"]);
    return result
}

/**
 * @type {number} interval - 间隔毫秒数
 */
function test(interval=3000){
    startTest();
    setInterval(startTest, interval);
    // alert(problems[0][0]);
    function startTest(){
        // document.write('<script src="https://cdn.jsdelivr.net/npm/jquery@3.4.0/dist/jquery.min.js"></script>');
        // document.write('<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full"></script>');
        var problems = getJSON('gradProb.json');
        var probLength = problems.length;
        // alert(probLength)
        var indexList = [];

        // 推荐算法 根据之前的错误率来推荐，还没算上最近的错误率
        for (var i = 0; i < probLength; i++){
            // indexList.push(i);
            if (problems[i][3] == 0) {
                for (var j = 0; j < problems[i][3] + 1; j++){
                    indexList.push(i);
                }
            }else {
                for (var j = 0; j < problems[i][3]; j++){
                    indexList.push(i);
                }
            }
        }

        // alert(indexList)
        randomIndexListIndex = Math.round(Math.random()*(indexList.length));
        var randomProblemsIndex = indexList[randomIndexListIndex]
        // alert(randomProblemsIndex)
        var oneProblem = problems[randomProblemsIndex]
        var correctAnswer = oneProblem[2];
        var falseNumber = oneProblem[3];
        var recentFalse = oneProblem[4].最近错过;
        // alert(typeof(recentFalse))

        var divTest = document.createElement('div');
        document.body.appendChild(divTest);
        divTest.id = 'popTest';
        var popTest = document.getElementById('popTest');
        popTest.style.width = '100%';
        popTest.style.height = '100%';
        popTest.style.color = 'black';
        popTest.style.position = 'fixed';
        popTest.style.top = '0';
        popTest.style.left = '0';
        popTest.style.backgroundColor = 'cadetblue';
        popTest.style.display = 'inline-block';

        var beginDate = new Date();
        var endDate = new Date('2022/12/24 0:0:1');
        var days = (endDate - beginDate) / (1000 * 60 * 60 * 24);
        var divCountDown = document.createElement('div');
        popTest.appendChild(divCountDown);
        divCountDown.id = 'countDown';
        var countDown = document.getElementById('countDown');
        countDown.innerHTML = '考研倒计时：' + days + '天';
        countDown.style.width = '100%';
        countDown.style.textAlign = 'center';
        countDown.style.fontSize = '40px';
        countDown.style.color = 'pink';
        countDown.style.position = 'fixed';

        var divQuestion = document.createElement('div');
        divQuestion.id = 'idQuestion';
        popTest.appendChild(divQuestion);
        var question = document.getElementById('idQuestion');
        question.innerHTML = oneProblem[0];
        question.style.textAlign = 'center';
        question.style.fontSize = '20px';
        // question.style.paddingTop = '39%';
        question.style.marginTop = '39%';

        var divFalseTimes = document.createElement('div');
        divFalseTimes.id = 'idFalseTimes';
        popTest.appendChild(divFalseTimes);
        var falseTimes = document.getElementById('idFalseTimes');
        falseTimes.innerHTML = '此题答错过' + falseNumber + '次';
        falseTimes.style.right = '5%';
        falseTimes.style.top = '20%';
        falseTimes.style.position = 'fixed';

        var divRecentFalse = document.createElement('div');
        divRecentFalse.id = 'idRecentFalse';
        popTest.appendChild(divRecentFalse);
        var recentFalseTimes = document.getElementById('idRecentFalse');
        recentFalseTimes.innerHTML = '最近错过' + recentFalse + '次';
        recentFalseTimes.style.right = '5%';
        recentFalseTimes.style.top = '25%';
        recentFalseTimes.style.position = 'fixed';
        
        var divChoices = document.createElement('div');
        divChoices.id = 'idChoices';
        popTest.appendChild(divChoices);
        var choices = document.getElementById('idChoices');
        choices.style.textAlign = 'center';
        choices.style.fontSize = '20px';
        choices.style.paddingTop = '20px';

        var divChoice1 = document.createElement('div');
        divChoice1.id = 'idChoice1';
        divChoices.appendChild(divChoice1);
        var choice1 = document.getElementById('idChoice1');
        choice1.innerHTML = oneProblem[1][0];

        var divChoice2 = document.createElement('div');
        divChoice2.id = 'idChoice2';
        divChoices.appendChild(divChoice2);
        var choice2 = document.getElementById('idChoice2');
        choice2.innerHTML = oneProblem[1][1];

        var divChoice3 = document.createElement('div');
        divChoice3.id = 'idChoice3';
        divChoices.appendChild(divChoice3);
        var choice3 = document.getElementById('idChoice3');
        choice3.innerHTML = oneProblem[1][2];

        var divChoice4 = document.createElement('div');
        divChoice4.id = 'idChoice4';
        divChoices.appendChild(divChoice4);
        var choice4 = document.getElementById('idChoice4');
        choice4.innerHTML = oneProblem[1][3];

        var choiceList = [choice1, choice2, choice3, choice4]

        for (var index in choiceList) {
            if (choiceList[index].innerHTML == correctAnswer) {
                choiceList[index].onclick = function(){
                    alert('答对了！');
                    if (recentFalse > 0) {
                        recentFalse -= 1;
                        $.post('/changeFalseNumber', {
                            questionNumber: randomProblemsIndex,
                            falseNumber: falseNumber,
                            recentFalse: recentFalse
                        });
                    }
                    document.getElementById('popTest').remove();
                }
            }else {
                choiceList[index].onclick = function(){
                    falseNumber += 1;
                    recentFalse += 1;
                    alert('你答错❌' + falseNumber +'次了！');
                    $.post('/changeFalseNumber', {
                        questionNumber: randomProblemsIndex,
                        falseNumber: falseNumber,
                        recentFalse: recentFalse
                    });
                }
            }
            if (choiceList[index] == choice4) {
                choiceList[index].style.marginRight = '0px';
            }else {
                choiceList[index].style.marginRight = '20px';
            }
            choiceList[index].style.cursor = 'pointer';
            choiceList[index].style.display = 'inline-block';
        }
    }
}