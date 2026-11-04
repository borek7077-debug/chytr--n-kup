# Partneři a XML feedy – ověřeno 4. 11. 2026

Tento seznam eviduje potvrzení e-mailem od affiliate manažerů eHUB. **Neznamená, že je feed již technicky napojen.** Před aktivací každého zdroje ověřit členství v programu, omezení propagace, URL feedu a funkčnost affiliate odkazu.

| Program | Stav programu | Potvrzení použití XML | Poznámka |
| --- | --- | --- | --- |
| Nářadí-Praha.cz | dříve schválen | dříve písemně potvrzeno | První ověřený zdroj |
| Nářadí-Simon.cz | schválení e-mailem 2026-10 | ano, podmíněno omezeními programu | Automatické načítání, ceny, fotografie, popisy i porovnání |
| Cubenest.cz | ověřit v eHUB | ano, 2026-11-02 | Potvrzeno stahování XML dle žádosti |
| Curele-ceas.ro | schváleno 2026-10-26 | ano, 2026-11-03 | Výslovně povoleno denní stahování |
| BATTEX.cz | schváleno 2026-10-22 | obecné stanovisko eHUB 2026-10-29 | Pouze je-li feed dostupný v programu |
| Venixvape.cz | dříve schválen | obecné stanovisko eHUB 2026-10-29 | Ověřit omezení programu |
| Cigaretycajk.cz | neověřeno | obecné stanovisko eHUB 2026-10-29 | Neaktivovat bez schválení a kontroly omezení |
| Berserkr.cz | neověřeno | obecné stanovisko eHUB 2026-10-29 | Neaktivovat bez schválení a kontroly omezení |
| Portál.cz | dříve schválen | individuální odpověď nedoložena | Urgence odeslána 2026-10-28; zachovat dříve funkční provizní přesměrování, pokud vyhovuje podmínkám |

## Affiliate odkazy
- eHUB manažer Robin Fanta potvrdil, že `a_aid` je stálé ID partnera, `a_bid` je **ID reklamního prvku konkrétního programu**, nikoliv ID účtu.
- Hodnoty `a_bid` se musí získat z https://pm.ehub.cz/creative ; nikdy je neodhadovat.
- `desturl` je URL konkrétního produktu.
- Některé eHUB XML feedy obsahují hotové affiliate URL; obyčejné URL produktů je třeba převést přes generátor odkazů.
- V katalogu nezobrazovat produkty bez ověřeného oprávnění a funkčního provizního odkazu.

## Další postup před spuštěním
1. V eHUB ověřit schválení všech programů, omezení a skutečné URL feedů.
2. Získat skutečné identifikátory reklamních prvků a otestovat přesměrování.
3. Připravit import s normalizací EAN, cen, dostupnosti, obrázků a deduplikací.
4. Aktualizace zatím **1× týdně v pondělí**, ne denně.
5. Nejprve otestovat katalog; **Netlify zatím nepřipojovat a nic nezveřejňovat**.

Zdroj: e-mailové odpovědi eHUB z 29. 10., 30. 10., 2. 11. a 3. 11. 2026.
