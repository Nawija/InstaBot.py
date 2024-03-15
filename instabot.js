const puppeteer = require("puppeteer");

let likedPhoto = 0;

const login = "Seovileo";
const pass = "Firekon1@";
const tags = [
    "stronawww",
    "stronainternetowa",
    "wroclaw",
    "warszawa",
    "biznes",
    "biznesonline",
    "wlasnybiznes",
    "motywacja",
    "marketing",
    "inspiracja",
    "polska",
];

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function randomSleep(min, max) {
    return Math.random() * (max - min) + min;
}

async function InstaLogic() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto("https://www.instagram.com/", {
        waitUntil: "networkidle2",
    });

    await page.click(
        "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_0"
    );

    await sleep(randomSleep(1000, 2000));

    await page.type(
        "#loginForm > div > div:nth-child(1) > div > label > input",
        login
    );

    await sleep(randomSleep(1000, 3000));

    await page.type(
        "#loginForm > div > div:nth-child(2) > div > label > input",
        pass
    );

    await sleep(randomSleep(1000, 3000));

    await page.click("#loginForm > div > div:nth-child(3)");

    const randomTag = tags[Math.floor(Math.random() * tags.length)];
    console.log("Random Tag:", randomTag);
    await sleep(randomSleep(12000, 14000));
    await page.goto(`https://www.instagram.com/explore/tags/${randomTag}`, {
        waitUntil: "networkidle2",
    });

    await sleep(randomSleep(7000, 10000));
    // Math.floor(Math.random() * 3)
    // Math.random() * (max - min)

    await page.click(
        "div > div > div > div > div > div > div > div > section > main > article > div > div > div > div:nth-child(1) > div:nth-child(1) > a > div"
    );
    await sleep(randomSleep(3000, 4000));
    const likeButton = await page.$('svg[aria-label*="Lubię to"]');
    if (likeButton) {
        // Kliknięcie przycisku "Lubię to"
        await likeButton.click();
    } else {
        console.log("Nie znaleziono przycisku 'Lubię to'.");
    }
    await sleep(randomSleep(3000, 4000));
    await page.click(
        "body > div > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div > button"
    );
    await sleep(randomSleep(3000, 4000));
    await page.click(
        "body > div > div > div > div > div > div > div > div > div > div > article > div > div > div > div > div > section > span > div > div > span > svg"
    );
    likedPhoto++;
    await sleep(randomSleep(3000, 4000));
    await page.click(
        "body > div > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > button"
    );

    console.log(`koniec test polubien:` + likedPhoto);
    await sleep(300000);
    // await browser.close();
}

async function main() {
    await InstaLogic(); // Dodaj await tutaj, aby poczekać na zakończenie checkJobOlx
}

main();
