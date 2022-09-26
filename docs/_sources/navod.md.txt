# Navod

## GitHub a GitPod

```{eval-rst}
.. automodule:: 26.09.2022
   :members:
```


1.	Zaregistrujte se na [GitHubu](https://github.com), ideálně přes univerzitní účet (pro případné uplatňování studentských slev)
2.	Personalizaci po registraci můžete viceméně ignorovat a prostě odklikat. Na konci ale zvolte **Continue using GitHub for free**
3.	Jděte na [repozitář se šablonou](https://github.com/ARostekMU/ultimatni-prirucka)
4.	Klikněte na **Fork** a poté **Create Fork**
5.	Jděte na [GitPod](https://www.gitpod.io/), klikněte na **Login** a **Continue with GitHub**
6.	Po otevření okna zvolte **Authorize gitpod-io**
7.	Jako IDE ponechte zvolený **VSCode BROWSER**. Pak **Continue**.
8.	Před URL forkovaného repozitáře z GitHubu přidejte *https://gitpod.io/#* a jděte na tuto adresu – otevře se workspace v GitPodu.
9.	Pravděpodobně vyskočí okno **User Validation Required**. Postupujte podle pokynů, zadejte tel. číslo a počkejte na povrzovaní kód, který budete muset vyplnit. Klik  **Validate account**.
10.	Otevřel se workspace – před sebou vidíte VSCode v prohlížeči s naklonovaným repozitářem z GitHubu. **Release notes** a **Get Started** můžete zavřít. Vlevo si volíte soubor, který chcete otevřít. Dole máte otevřený terminál, který můžete otevřít/zavřít pomocí *Ctrl+`*
11.	Když vyskočí okno s **Recommended Extension for Python**, s radostí ji nainstalujte.
12.	Abychom mohli začít vyvíjet, je potřeba nainstalovat všechny potřebné balíčky. Toho lze docílit pomocí příkazu `poetry install`. Toto ale pochopitelně nechceme dělat pokaždé! GitPod by nám měl ideálně připravit takový workspace, ve kterém instalace již proběhla. Je proto potřeba drobná konfigurace...
13.	Do terminálu napište `gp init`. Tento příkaz vytvoří výchozí soubor *.gitpod.yml*
14.	Smažte všechno kromě řádků *tasks* a *init* a příkaz za init přepište na *poetry install*. GitPod díky tomu bude vědět, že každý nový workspace by měl udělat `poetry install`. Ale pozor! Je potřeba tyto změny tzv. commitnout, jinak se neprojeví.
15.	`git status` ukáže, které gitem trackované soubory se změnily, příp. které soubory gitem trackované nejsou. V tomto případě se ukáže *.gitpod.yml* jako untracked file.
16.	`git add .gitpod.yml` tento soubor přidá mezi tzv. changes to be commited, o čemž se můžeme předsvědčit opětovným `git status`
17.	`git commit` tyto změny tzv. commitne. Ideálně by měla každý commit doprovázet nějaká zpráva, která vystihuje provedené změny, v našem případě např. `git commit -m “added poetry install command in .gitpod.yml”`
18.	`git log` nám ukáže historii všech commitů – měli byste tam vidět také svůj nejnovější commit. Tento commit je ale zatím pouze v tomto workspace, v repozitáři na GitHubu se zatím neprojevil
19.	`git push` pošle lokální commity do GitHub repozitáře. Toto ale zatím nefunguje, protože jsme to GitPodu nedovolili
20.	Jděte do [GitPod Integrations](https://gitpod.io/integrations) a v řádku GitHub klikněte na **tři tečky** -> **Edit Permissions**. Zaškrtněte všechno -> **Update Permissions** -> **Authorize gitpod-io**
21.	`git push` nyní funguje. Po otevření svého repozitáře v GitHubu byste měli vidět, že je v něm nový commit a soubor *.gitpod.yml* existuje
22.	Pro větší comfort a snadné otevírání GitPodu přímo z GitHubu si můžete do prohlížeče nainstalovat GitPod extension, pro Chrome např. [tady](https://www.gitpod.io/docs/browser-extension/)
23.	Po nainstalování byste měli u svého repozitáře v GitHubu vidět zelený button **GitPod**. Kliknutím na něj se otevřene daný repozitář v GitPodu.
24.	Pokud jste všechno udělali správně, měli byste v terminálu vidět, že `poetry install` proběhlo automaticky. Zkuste použít nějaký příkaz, např. `poetry run pytest` nebo `poetry run ultimatni-prirucka`
