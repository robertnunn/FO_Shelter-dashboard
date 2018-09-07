# FO_Shelter-dashboard
Decrypts, extracts, and presents a high-level overview of a fallout shelter vault.
Data is visualized in MS Excel

Python script decrypts and extracts data to a set of .csv files (inventory, dwellers, resources). Excel document automatically pulls the data from these .csv files upon opening and presents a high-level overview of the vault. Dweller data is presented in a set of three pivot tables that break down dwellers by weapon equipped, outfit equipped, and the room they're assigned to. Inventory data is also presented in a pivot table and broken down by the same categories as in the game: weapons, outfits, pets, and junk.

More detailed information on individual dwellers is found on the "Vault Dwellers" tab. Here you can find all the basic stats (Name, sex, level, SPECIAL, etc) as well as a couple calculated stats: potential and average damage. Potential indicates what percentage of the maximum possible health (644) this particular dweller can achieve. For example, if a dweller has a potential of 79%, you would know that even under the best possible circumstances, this dweller could only have a maximum of 509 HP at level 50. 

There are additional tabs that list all the items in the game (weapons, outfits, etc) as well as the lookup tables. If a tab has "sortable" in the name, these data can be freely manipulated without affecting the lookups in other tabs. Otherwise, changing the data, even just by resorting, can produce non-sensical results in other tabs (specifically, the "Dwellers" tab).
