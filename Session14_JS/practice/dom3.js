const dc = document;
const myList = dc.querySelector(".myList");

for (let i = 1; i <= 3; i++) {
  let item = dc.createElement("li");
  item.innerText = i + "번째 추가 항목";
  myList.append(item);
}
