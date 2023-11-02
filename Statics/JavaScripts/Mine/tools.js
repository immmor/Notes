// document.write('<script src="{{url_for("static", filename ="JavaScripts/Others/jquery.js")}}"></script>');
document.write('<script src="Statics/JavaScripts/Others/jquery.js"></script>');
document.write('<script src="Statics/JavaScripts/Others/tex-mml-chtml.js"></script>');

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
    function startTest(){
        var problems = getJSON('/Statics/Others/gradProb.json');
        var probLength = problems.length;
        var indexList = [];

        // 推荐算法 根据之前的错误率来推荐，还没算上最近的错误率
        for (var i = 0; i < probLength; i++){
            if (problems[i][3] == 0) {
                for (var j = 0; j < problems[i][3] + 1; j++){
                    indexList.push(i);
                }
            } else {
                for (var j = 0; j < problems[i][3]; j++){
                    indexList.push(i);
                }
            }
        }

        randomIndexListIndex = Math.round(Math.random()*(indexList.length));
        var randomProblemsIndex = indexList[randomIndexListIndex]
        var oneProblem = problems[randomProblemsIndex]
        var correctAnswer = oneProblem[2];
        var falseNumber = oneProblem[3];
        var recentFalse = oneProblem[4].最近错过;

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
        var endDate = new Date('2023/12/24 0:0:1');
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
        question.style.marginTop = '25%';
        // question.style.marginBottom = '29%';

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
// test(300000);

function new_test(interval=300000){
    document.addEventListener('DOMContentLoaded', function() {
        // 在这里执行你的脚本代码
        startTest();
        setInterval(startTest, interval);
        function startTest(){
            var rawProblems = getJSON('/Statics/Others/gradProb.json');  //TODO 得改地址
            var problems = rawProblems['考研题目']
            var probLength = problems.length;
            var indexList = [];

            // 推荐算法 根据之前的错误率来推荐，还没算上最近的错误率
            for (var i = 0; i < probLength; i++){
                if (problems[i]["错误次数"] == 0) {
                    for (var j = 0; j < problems[i]["错误次数"] + 1; j++){
                        indexList.push(i);
                    }
                } else {
                    for (var j = 0; j < problems[i]["错误次数"]; j++){
                        indexList.push(i);
                    }
                }
            }

            randomIndexListIndex = Math.round(Math.random()*(indexList.length));
            var randomProblemsIndex = indexList[randomIndexListIndex]
            var oneProblem = problems[randomProblemsIndex]
            var correctAnswer = oneProblem["答案"];
            var falseNumber = oneProblem["错误次数"];
            var recentFalse = oneProblem["最近错过"];

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
            var endDate = new Date('2023/12/24 0:0:1');
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
            question.innerHTML = oneProblem["问题"];
            question.style.textAlign = 'center';
            question.style.fontSize = '20px';
            question.style.marginTop = '25%';
            // question.style.marginBottom = '29%';

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

            // 4个数里随机挑一个，被选的数字下一次不可被选
            var availableNumbers = [0, 1, 2, 3];
            function getRandomNumber() {
                if (availableNumbers.length === 0) {
                    return null; // 所有数字都已经获取完毕
                }
                var randomIndex = Math.floor(Math.random() * availableNumbers.length);
                var randomNumber = availableNumbers[randomIndex];
                availableNumbers.splice(randomIndex, 1); // 从可用数字列表中移除已获取的数字
                return randomNumber;
            }

            var divChoice1 = document.createElement('div');
            divChoice1.id = 'idChoice1';
            divChoices.appendChild(divChoice1);
            var choice1 = document.getElementById('idChoice1');
            choice1.innerHTML = 'A、' + oneProblem["选项"][getRandomNumber()].slice(2);

            var divChoice2 = document.createElement('div');
            divChoice2.id = 'idChoice2';
            divChoices.appendChild(divChoice2);
            var choice2 = document.getElementById('idChoice2');
            choice2.innerHTML = 'B、' + oneProblem["选项"][getRandomNumber()].slice(2);

            var divChoice3 = document.createElement('div');
            divChoice3.id = 'idChoice3';
            divChoices.appendChild(divChoice3);
            var choice3 = document.getElementById('idChoice3');
            choice3.innerHTML = 'C、' + oneProblem["选项"][getRandomNumber()].slice(2);

            var divChoice4 = document.createElement('div');
            divChoice4.id = 'idChoice4';
            divChoices.appendChild(divChoice4);
            var choice4 = document.getElementById('idChoice4');
            choice4.innerHTML = 'D、' + oneProblem["选项"][getRandomNumber()].slice(2);

            var choiceList = [choice1, choice2, choice3, choice4]

            $.post('/showTimes', {
                questionNumber: randomProblemsIndex,
            });

            for (var index in choiceList) {
                if (choiceList[index].innerHTML.slice(2) == correctAnswer.slice(2)) {
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
                        falseTimes.innerHTML = '此题答错过' + falseNumber + '次';
                        recentFalse += 1;
                        recentFalseTimes.innerHTML = '最近错过' + recentFalse + '次';
                        setTimeout(function() {
                            alert('你答错❌' + falseNumber + '次了！');
                        }, 1);
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
    });
    
}
new_test();

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

function loginin() {
    var divLogin = document.createElement('div');
    document.body.appendChild(divLogin);
    divLogin.id = 'login';
    document.getElementById("login").classList.add("log");
    document.getElementById("login").classList.add("login");
    document.getElementById("login").innerHTML = '<div class="login-box"><h2>登  录</h2><form><div class="user-box"><input type="text" id="username"><label>用户名</label></div><div class="user-box"><input type="password" id="passwordid"><label>密码</label></div><div class="register" id="registerInLogin" onclick="register()">新用户注册</div><a id="submit"><span></span><span></span><span></span><span></span>提 交</a></form></div>'
    let cookieKeys = document.cookie.match(/[^ =;]+(?=\=)/g); 
    // alert(cookieKeys)
    // let hasUserInfo = cookieKeys.indexOf('userInfo')
    if (!cookieKeys) {
        document.getElementById('logout').style.display = 'none';
        document.getElementById('login').style.display = 'block';
        $('#submit').click(function() { //点击按钮
            var username = hex_md5(document.getElementById('username').value)
            var password = hex_md5(document.getElementById('passwordid').value)
            $.post('/login', {
                username: username,
                password: password,
                subjectName: subjectName
            }).then(function(response) {
                    if (response == 'fail') {
                        alert('用户名密码不存在')
                    }else {
                        setCookie('userInfo', username + "|" + password, 10)
                        document.getElementById('login').style.display = 'none';
                        document.getElementById('logout').style.display = 'block';
                    }
            });
        })
    }else {
        document.getElementById('logout').style.display = 'block';
        cookie = document.cookie
        cookieList = cookie.split('=')
        $.post('/login', {
            username: cookieList[0],
            password: cookieList[1],
            subjectName: subjectName
        })
    }
}

function logout() {
    clearCookie(document.cookie.split("=")[0]);
    location.reload();
}

function setCookie(cname, cvalue, exdays){
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

// 删除cookie
function clearCookie(name) {
    setCookie(name, "", -1);
}

function notify() {
    var divNotify = document.createElement('div');
    document.body.appendChild(divNotify);
    divNotify.id = 'notify';
    var notify = document.getElementById('notify');
    notify.style.border = '2px solid red';
    notify.style.margin = '0 auto'
    notify.style.width = '300px';
    notify.style.height = '80px';
    notify.style.display = 'flex';
    notify.style.justifyContent = 'center';
    notify.style.alignItems = 'center';
    notify.style.textAlign = 'center';
    notify.style.backgroundColor = 'red';
    notify.style.top = '2%';
    notify.style.left = '50%'
    notify.style.color = 'white';
    notify.style.position = 'absolute';
    notify.innerText = '干大法师大法师的'
}

// TODO
function hotkey_search() {
    document.addEventListener("keydown", function(event) {
        if (event.ctrlKey && (event.key === "k" || event.key === "K")) {
            event.preventDefault(); // 阻止默认行为
            let searchQuery = prompt("搜点什么？");
            if (searchQuery) {
                if (searchQuery.startsWith('百度：')) {
                    let searchUrl = `https://www.baidu.com/s?wd=${encodeURIComponent(searchQuery)}`;
                    window.open(searchUrl, "_blank");
                } else if (searchQuery.startsWith('谷歌：')) {
                    let searchUrl = `https://www.google.com/search?q=${encodeURIComponent(searchQuery)}`;
                    window.open(searchUrl, '_blank');
                } else if (searchQuery.startsWith('翻译：')) {
                    let content = searchQuery.split('：').pop();
                    let searchUrl = `https://fanyi.baidu.com/translate?aldtype=16047&query=${encodeURIComponent(content)}&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/${encodeURIComponent(content)}`
                    window.open(searchUrl, '_blank');
                } else {
                    let searchUrl = `https://www.baidu.com/s?wd=${encodeURIComponent(searchQuery)}`;
                    window.open(searchUrl, "_blank");
                }
            } else {}
        }
    });
}
hotkey_search()

function dot() {
    // Create div for dot 
    const dot = document.getElementById("dot");
    dot.style.width = "100px";
    dot.style.height = "100px";
    dot.style.backgroundColor = "red";
    dot.style.borderRadius = "50%"; 
    dot.style.position = "relative";

    // Add to body
    document.body.appendChild(dot); 

    // Track position
    let x = 0;
    let y = 0;

    // Handle keydown
    document.addEventListener("keydown", (e) => {
        switch (e.key) {
            case "ArrowUp":
            y -= 10;
            break;
            case "ArrowDown":
            y += 10;
            break;
            case "ArrowLeft":
            x -= 10;
            break;
            case "ArrowRight": 
            x += 10;
            break;
        }
        
        // Update position
        dot.style.left = x + "px";
        dot.style.top = y + "px";
    });
}

/**
 * 监听整个文档的点击事件。
 * 当某个元素被选中，则给服务器返回它的id和class
 */
function listen() {
    // 监听整个文档的点击事件
    document.addEventListener('click', event => {
        // 获取被点击的元素
        const target = event.target;
        const title = document.title;
        const currentUrl = window.location.href;
        // 检查 id 和 class
        if(target.id || target.className) {
            // 构造弹出内容
            let clickedElement = '';
            if (target.id) {
                clickedElement += `id:${target.id} `;
            }
            if (target.className) {
                clickedElement += `class:${target.className}`; 
            }
            $.post('/listen', {
                clickedElement: clickedElement,
                title: title,
                currentUrl: currentUrl
            });
        }
    });
}
listen()

function comment() {
    document.addEventListener('DOMContentLoaded', function() {
        var divComment = document.createElement('div');
        document.body.appendChild(divComment);
        // divComment.id = 'comment';
        divComment.classList.add('comment');
        divComment.innerHTML = '评论<div class="closeComment">关闭</div>';

        document.querySelector('.closeComment').addEventListener('click', function() {
            document.querySelector('.comment').style.left = '-300px'; // 将 .comment 元素隐藏在视图之外
        });

        document.addEventListener('mousemove', function(event) {
            let mouseX = event.clientX;
            let mouseY = event.clientY;
            let windowHeight = window.innerHeight;
            if (mouseX <= 10 && mouseY >= windowHeight * 0.3 && mouseY <= windowHeight * 0.7) {
                document.querySelector('.comment').style.left = '0';
            }
        });
    });
}
comment()