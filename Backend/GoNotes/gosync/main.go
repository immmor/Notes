package main

import (
	"fmt"
	"log"
	"sync"
	"time"
)

type HouseInfo struct {
	ID            int
	Owners        []string
	Price         int
	BacnkAccounts []int
	OwnersMoney   int
}

const Owners = "Owners"
const Price = "Price"
const BacnkAccounts = "BacnkAccounts"

type Response struct {
	data map[string]any
	err  error
}

func sellHouseInfo(id int) (*HouseInfo, error) {
	respch := make(chan Response, 3)
	wg := &sync.WaitGroup{}
	wg.Add(3)
	go tenementinfoForOwners(id, respch, wg)
	go taobaoForPrice(id, respch, wg)
	go BankForBankAccount(id, respch, wg)
	wg.Wait()
	close(respch)
	houseInfo := &HouseInfo{}
	responseMap := make(map[string]any, 3)

	for resp := range respch {
		if resp.err != nil {
			return nil, resp.err
		}
		for key, value := range resp.data {
			responseMap[key] = value
		}
	}

	houseInfo.Owners = responseMap[Owners].([]string)
	// houseInfo.Owners = responseMap[Owners].{[]string}

	houseInfo.Price = responseMap[Price].(int)
	houseInfo.BacnkAccounts = responseMap[BacnkAccounts].([]int)
	return houseInfo, nil
}

func BankForBankAccount(id int, respch chan Response, wg *sync.WaitGroup) {
	time.Sleep(time.Millisecond * 2023)
	cardIds := []int{1312121, 1212372, 1923312}
	respch <- Response{
		data: map[string]any{BacnkAccounts: cardIds},
		err:  nil,
	}
	wg.Done()
}

func taobaoForPrice(id int, respch chan Response, wg *sync.WaitGroup) {
	time.Sleep(time.Millisecond * 2023)
	respch <- Response{
		data: map[string]any{Price: 400000},
		err:  nil,
	}
	wg.Done()
}

func tenementinfoForOwners(id int, respch chan Response, wg *sync.WaitGroup) {
	time.Sleep(time.Millisecond * 2023)
	users := []string{"zhangsan", "zhangsan's shadow"}
	respch <- Response{
		data: map[string]any{Owners: users},
		err:  nil,
	}
	wg.Done()
}

func unpayHouseloan(cards []int) int {
	return len(cards) * 200000
}

func storeData(house *HouseInfo) {
	fmt.Printf("%+v\n", house)
	fmt.Println("store data success")
}

func main() {
	start := time.Now()
	houseInfo, err := sellHouseInfo(132324324)
	if err != nil {
		log.Fatal(err)
	}
	houseInfo.OwnersMoney = houseInfo.Price - unpayHouseloan(houseInfo.BacnkAccounts)
	storeData(houseInfo)
	fmt.Println("used time: ", time.Since(start))
}
