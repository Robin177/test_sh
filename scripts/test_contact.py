from appium import webdriver
import pytest
import allure


class TestContact:
    @allure.severity("bloker")
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        allure.attach("登录", "登录的描述")
        print("点击登录")

        assert 0

    @allure.severity("critical")
    @allure.step(title="用户名的测试脚本")
    def test_username(self):

        assert 1

    @allure.severity("trivial")
    @allure.step(title="密码的测试脚本")
    def test_passwo1d(self):

        assert 1
        
        
     
