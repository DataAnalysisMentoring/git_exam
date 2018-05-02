# Zkouška praktických dovedností s gitem

Zkouška je rozdělena na následující části.

## Vytvoření vlastního repozitáře

1) Úkolem je vytvořit na githubu vlastní repozitář s libovolným jménem.
   Repozitář stáhnout k sobě a následující kroky dělat jen u sebe.
2) Naplnit ho libovolným souborem jako vstupní commit.
3) Soubor postupně editovat a každou ucelenou změnu potvrdit commitem. Cíl je mít hezkou historii v mastru. Stačí 2-3 commity.
4) Další změna souboru proběhne v nové větvi. Větev může mít libovolné jméno.
5) Změna z větve z předchozího kroku je mergem připojena do mastera. (Bez PR)
6) Další změna jde opět do nové větve. S velkým rozdílem. Tentokrát je třeba změnu provést na dvou
   místech: V nové větvi a v masteru. Cíl je vytvořit konflikt - znamená to udělat podobnou změnu
   na tom samém řádku v masteru i ve větvi.
7) Když jsou obě dvě změny potvrzeny commitem ve své větvi. Provést merge a vyřešit vzniklý konflikt.
8) Zopakovat krok 6, tedy opět novou větev a změnu v masteru a ve větvi.
9) Když jsou obě dvě změny commitnuty. Přednout se do větve a provést rebase na mastera.
   Konflikt vyřešit.
10) Přednout se do mastera a mergnout větev
11) Pushnout do repozitáře.
12) Radovat se.

## Forknutí tohoto repozitáře

1) Začít forkem tohoto repozitáře.
2) Stáhnout svůj nový repozitář k sobě.
3) Vytvořit novou větev a v ní přidat nový soubor, libovolný.
4) Zkontrolovat jestli není nová verze v původním repozitáři (Část návodu je prezentaci, zbytek bude je
   potřeba pohledat, až jako poslední možnost poradím.).
5) Stáhnout nové změny do svého mastera.
6) Provést rebase větve na nového mastera.
7) Pushnout větev k sobe do repozitáře.
8) Vytvořit PR z nové vzniklé větve do původního repozitáře.
9) Počkat jeslti nebudou připomínky, pokud budou opravit je.
10) Když je větev mergnutá, radovat se.
