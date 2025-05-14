const x = `x = <input type="text" name="x" id="x" placeholder="Введите корень уравнения" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center;  position: relative; top: -7px;"><br>`
const x2 = `x₁ = <input type="text" name="x1" id="x1" placeholder="Введите один из корней" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; position: relative; top: -7px;"><br>x₂ = <input type="text" name="x2" id="x2" placeholder="Введите второй из корней" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; position: relative; top: -7px;"><br>`
const x4 = `x₁ = <input type="text" name="x1" id="x1" placeholder="Введите 1-й корень" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; width: 146px; position: relative; top: -7px;"><br>x₂ = <input type="text" name="x2" id="x2" placeholder="Введите 2-й корень" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; width: 146px; position: relative; top: -7px;"><br>x₃ = <input type="text" name="x3" id="x3" placeholder="Введите 3-й корень" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; width: 146px; position: relative; top: -7px;"><br>x₄ = <input type="text" name="x4" id="x4" placeholder="Введите 4-й корень" style="height: 35px; border: 0.2em solid black; border-radius: 20px; text-align: center; width: 146px; position: relative; top: -7px;"><br>`

const select1 = document.querySelector('.select-1');
select1.onchange = function() {
    let item = select1.value;
    if (item == 'k2') {
        document.querySelector(".xzdes").innerHTML = x2;
    } else if (item == 'k1') {
        document.querySelector(".xzdes").innerHTML = x;
    } else if (item == 'k4') {
        document.querySelector(".xzdes").innerHTML = x4;
    } else {
        document.querySelector(".xzdes").innerHTML = `Корней нет <br>`;
    }
}