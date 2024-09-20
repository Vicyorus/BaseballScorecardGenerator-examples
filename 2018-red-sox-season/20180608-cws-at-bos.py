import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2018-06-08
# https://www.baseball-reference.com/boxes/BOS/BOS201806080.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2018/06/08/530346/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-08 19:11-21:35",
        "at": "Fenway Park, Boston, MA",
        "att": "36,593",
        "temp": "70F, Partly Cloudy",
        "wind": "6mph, R To L",
        "away": {
            "team": "Chicago White Sox",
            "starter": 68,
            "roster": {
                # Lineup
                7: "Tim Anderson",
                20: "José Rondón",
                79: "José Abreu",
                24: "Matt Davidson",
                36: "Kevan Smith",
                10: "Yoán Moncada",
                32: "Trayce Thompson",
                18: "Daniel Palka",
                22: "Charles Tilson",
                # Starting pitcher
                68: "Dylan Covey",
                # Bench
                38: "Omar Narváez",
                5: "Yolmer Sánchez",
                15: "Adam Engel",
                # Bullpen
                65: "Nate Jones",
                52: "Xavier Cedeño",
                48: "Joakim Soria",
                33: "James Shields",
                54: "Chris Beck",
                40: "Reynaldo López",
                57: "Jace Fry",
                66: "Chris Volstad",
                27: "Lucas Giolito",
                53: "Héctor Santiago",
                70: "Luis Avilán",
                44: "Bruce Rondón",
            },
            "lefties": [52, 57, 53, 70],
            "lineup": [
                [7, "6"],
                [20, "5"],
                [79, "3"],
                [24, "0"],
                [36, "2"],
                [10, "4"],
                [32, "8"],
                [18, "9"],
                [22, "7"],
            ],
            "bench": [
                [38, "C"],
                [5, "3B"],
                [15, "CF"],
            ],
            "bullpen": [65, 52, 48, 33, 54, 40, 57, 66, 27, 53, 70, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                12: "Brock Holt",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                3: "Sandy León",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                59: "Sam Travis",
                28: "J.D. Martinez",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 61, 24],
            "lineup": [
                [16, "7"],
                [12, "9"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [19, "8"],
                [23, "0"],
                [3, "2"],
            ],
            "bench": [
                [59, "1B"],
                [28, "DH"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "Jeff Kellogg",
            "1B": "Shane Livensparger",
            "2B": "James Hoye",
            "3B": "Quinn Wolcott",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. CWS #7  Tim Anderson (X - X - X)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 2. CWS #20 José Rondón (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b")
t1.out("G6-3")

# 3. CWS #79 José Abreu (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b b")
t1.reach("BB")

# 4. CWS #24 Matt Davidson (X - X - 79)
t1.new_ab()
t1.pitch_list("c b b b f c")
t1.out("!K")


# Bot 1st
# Pitching: CWS #68 Dylan Covey
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b f f b")
b1.hit(2)

# 2. BOS #12 Brock Holt (X - 16 - X)
b1.new_ab()
b1.pitch_list("b b s b c f b")
b1.reach("BB")
b1.thrown_out(2, "18 DP3-6-1", 2, 68)

# 3. BOS #2  Xander Bogaerts (X - 16 - 12)
b1.new_ab()
b1.pitch_list("b c b f 2 s")
b1.out("K")

# 4. BOS #18 Mitch Moreland (X - 16 - 12)
b1.new_ab()
b1.out("DP3-6-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 5. CWS #36 Kevan Smith (X - X - X)
t2.new_ab()
t2.pitch_list("s s")
t2.out("G5-3")

# 6. CWS #10 Yoán Moncada (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")

# 7. CWS #32 Trayce Thompson (X - X - X)
t2.new_ab()
t2.pitch_list("c f b s")
t2.out("K")


# Bot 2nd
# Pitching: CWS #68 Dylan Covey
b2 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b")
b2.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("G5-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 8. CWS #18 Daniel Palka (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.out("G4-3")

# 9. CWS #22 Charles Tilson (X - X - X)
t3.new_ab()
t3.pitch_list("c f b s")
t3.out("K")

# 1. CWS #7  Tim Anderson (X - X - X)
t3.new_ab()
t3.pitch_list("s b")
t3.hit(1)

# 2. CWS #20 José Rondón (X - X - 7)
t3.new_ab()
t3.pitch_list("f b c s")
t3.out("K")


# Bot 3rd
# Pitching: CWS #68 Dylan Covey
b3 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c f")
b3.out("G4-3")

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c f c")
b3.out("!K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 3. CWS #79 José Abreu (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G3-1")

# 4. CWS #24 Matt Davidson (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")

# 5. CWS #36 Kevan Smith (X - X - X)
t4.new_ab()
t4.pitch_list("b c t")
t4.hit(1)

# 6. CWS #10 Yoán Moncada (X - X - 36)
t4.new_ab()
t4.pitch_list("s b f f d s")
t4.out("K")


# Bot 4th
# Pitching: CWS #68 Dylan Covey
b4 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("c b c f s")
b4.out("K")

# 3. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("f b c")
b4.out("F7")

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 7. CWS #32 Trayce Thompson (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c c f")
t5.out("F9")

# 8. CWS #18 Daniel Palka (X - X - X)
t5.new_ab()
t5.pitch_list("f c b s")
t5.out("K")

# 9. CWS #22 Charles Tilson (X - X - X)
t5.new_ab()
t5.pitch_list("c s f b f")
t5.out("G6-3")


# Bot 5th
# Pitching: CWS #68 Dylan Covey
b5 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f s b f")
b5.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.hit(2)

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b5.new_ab()
b5.pitch_list("b b f c c")
b5.out("!K")

# 8. BOS #23 Blake Swihart (X - 11 - X)
b5.new_ab()
b5.pitch_list("f b b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 1. CWS #7  Tim Anderson (X - X - X)
t6.new_ab()
t6.out("L9")

# 2. CWS #20 José Rondón (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.thrown_out(2, "79 FC6-4", 2, 41)

# 3. CWS #79 José Abreu (X - X - 20)
t6.new_ab()
t6.pitch_list("c b")
t6.reach("FC6-4")

# 4. CWS #24 Matt Davidson (X - X - 79)
t6.new_ab()
t6.out("G3")


# Bot 6th
# Pitching: CWS #68 Dylan Covey
b6 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.out("G3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("c b b s")
b6.out("F7")

# 2. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("f c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 Chris Sale
t7 = game.new_inning()

# 5. CWS #36 Kevan Smith (X - X - X)
t7.new_ab()
t7.hit(2)
t7.advance(3, "10 G4-3")
t7.advance(4, "32 1B")

# 6. CWS #10 Yoán Moncada (X - 36 - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G4-3")

# 7. CWS #32 Trayce Thompson (36 - X - X)
t7.new_ab()
t7.pitch_list("b c b s")
t7.hit(1, rbis=1)
t7.advance(2, "22 1B")
t7.thrown_out(2, "7 PO", 3, 41)

# 8. CWS #18 Daniel Palka (X - X - 32)
t7.new_ab()
t7.pitch_list("s c b s")
t7.out("K")

# 9. CWS #22 Charles Tilson (X - X - 32)
t7.new_ab()
t7.pitch_list("1 f")
t7.hit(1)

# 1. CWS #7  Tim Anderson (X - 32 - 22)
t7.new_ab()
t7.pitch_list("s s 2")
t7.no_ab("PO")


# Bot 7th
# Pitching: CWS #68 Dylan Covey
b7 = game.new_inning()

# 3. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)
b7.thrown_out(2, "18 FC3-5", 1, 57)

# Pitching change (CWS): #57 Jace Fry replaces #68 Dylan Covey
b7.pitching_substitution(57)

# 4. BOS #18 Mitch Moreland (X - X - 2)
b7.new_ab()
b7.pitch_list("c b")
b7.reach("FC3-5")
b7.error(5)
b7.advance(2, "36 E5")

# 5. BOS #36 Eduardo Núñez (X - X - 18)
b7.new_ab()
b7.pitch_list("b b")
b7.reach("FC5")

# 6. BOS #11 Rafael Devers (X - 18 - 36)
b7.new_ab()
b7.pitch_list("b s s s")
b7.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - 18 - 36)
b7.new_ab()
b7.pitch_list("d b c b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #41 Chris Sale
t8 = game.new_inning()

# 1. CWS #7  Tim Anderson (X - X - X)
t8.new_ab()
t8.pitch_list("b t b b")
t8.out("G1-3")

# 2. CWS #20 José Rondón (X - X - X)
t8.new_ab()
t8.pitch_list("s f s")
t8.out("K")

# 3. CWS #79 José Abreu (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G5-3")


# Bot 8th
# Pitching: CWS #65 Nate Jones
b8 = game.new_inning()

# Pitching change (CWS): #65 Nate Jones replaces #57 Jace Fry
b8.pitching_substitution(65)

# 8. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("s s b f s")
b8.out("K")

# 9. BOS #3  Sandy León (X - X - X)
b8.new_ab()
b8.pitch_list("s c")
b8.out("G6-3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #37 Heath Hembree
t9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #41 Chris Sale
t9.pitching_substitution(37)

# 4. CWS #24 Matt Davidson (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f s")
t9.out("K")

# 5. CWS #36 Kevan Smith (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b b")
t9.out("G5-3")

# 6. CWS #10 Yoán Moncada (X - X - X)
t9.new_ab()
t9.pitch_list("c c f s")
t9.out("K")


# Bot 9th
# Pitching: CWS #48 Joakim Soria
b9 = game.new_inning()

# Pitching change (CWS): #48 Joakim Soria replaces #65 Nate Jones
b9.pitching_substitution(48)

# 2. BOS #12 Brock Holt (X - X - X)
b9.new_ab()
b9.pitch_list("b c b c")
b9.out("L5")

# 3. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c c f b")
b9.out("P6")

# 4. BOS #18 Mitch Moreland (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G4-3")

# Winning team: CWS
# WP: CWS #68 Dylan Covey
game.winning_pitcher(68, is_away_team=True)
# SV: CWS #48 Joakim Soria
game.save_pitcher(48, is_away_team=True)

# Loser team: BOS
# LP: BOS #41 Chris Sale
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
