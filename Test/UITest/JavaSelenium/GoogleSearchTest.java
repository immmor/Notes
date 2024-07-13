import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class GoogleSearchTest {
    private WebDriver driver;

    @BeforeClass
    public void setUp() {
        // 设置 ChromeDriver 的路径
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
        driver = new ChromeDriver();
    }

    @Test
    public void searchForSelenium() {
        // 打开 Google 主页
        driver.get("https://www.google.com");

        // 找到搜索框并输入 "Selenium"
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys("Selenium");

        // 提交表单
        searchBox.submit();

        // 验证搜索结果页包含 "Selenium" 关键字
        String pageTitle = driver.getTitle();
        Assert.assertTrue(pageTitle.contains("Selenium"), "Search results do not contain 'Selenium'");
    }

    @AfterClass
    public void tearDown() {
        // 关闭浏览器
        driver.quit();
    }
}