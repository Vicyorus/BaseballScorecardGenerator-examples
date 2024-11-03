import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CWS @ BOS, 2018-06-10
# https://www.baseball-reference.com/boxes/BOS/BOS201806100.shtml
# https://www.mlb.com/gameday/white-sox-vs-red-sox/2018/06/10/530376/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-10 13:07-16:22",
        "at": "Fenway Park, Boston, MA",
        "att": "36,998",
        "temp": "67F, Sunny",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Chicago White Sox",
            "starter": 40,
            "roster": {
                # Lineup
                10: "Yoán Moncada",
                5: "Yolmer Sánchez",
                79: "José Abreu",
                18: "Daniel Palka",
                24: "Matt Davidson",
                38: "Omar Narváez",
                7: "Tim Anderson",
                22: "Charles Tilson",
                32: "Trayce Thompson",
                # Starting pitcher
                40: "Reynaldo López",
                # Bench
                20: "José Rondón",
                15: "Adam Engel",
                36: "Kevan Smith",
                # Bullpen
                65: "Nate Jones",
                55: "Carlos Rodón",
                52: "Xavier Cedeño",
                48: "Joakim Soria",
                33: "James Shields",
                68: "Dylan Covey",
                57: "Jace Fry",
                66: "Chris Volstad",
                27: "Lucas Giolito",
                53: "Héctor Santiago",
                70: "Luis Avilán",
                44: "Bruce Rondón",
            },
            "lefties": [55, 52, 57, 53, 70],
            "lineup": [
                [10, "4"],
                [5, "5"],
                [79, "0"],
                [18, "9"],
                [24, "3"],
                [38, "2"],
                [7, "6"],
                [22, "7"],
                [32, "8"],
            ],
            "bench": [
                [20, "SS"],
                [15, "CF"],
                [36, "C"],
            ],
            "bullpen": [65, 55, 52, 48, 33, 68, 57, 66, 27, 53, 70, 44],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                36: "Eduardo Núñez",
                59: "Sam Travis",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [12, "4"],
                [19, "8"],
                [23, "9"],
                [3, "2"],
            ],
            "bench": [
                [36, "SS"],
                [59, "1B"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "umpires": {
            "HP": "James Hoye",
            "1B": "Quinn Wolcott",
            "2B": "Jeff Kellogg",
            "3B": "Shane Livensparger",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. CWS #10 Yoán Moncada (X - X - X)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "5 FC3-6", 1, 22)

# 2. CWS #5  Yolmer Sánchez (X - X - 10)
t1.new_ab()
t1.pitch_list("c")
t1.reach("FC3-6")
t1.advance(4, "79 2B")

# 3. CWS #79 José Abreu (X - X - 5)
t1.new_ab()
t1.pitch_list("b c f b 1 1 f b f")
t1.hit(2, rbis=1)
t1.advance(3, "18 G3-1")

# 4. CWS #18 Daniel Palka (X - 79 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s b")
t1.out("G3-1")

# 5. CWS #24 Matt Davidson (79 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s b b t b s")
t1.out("K")


# Bot 1st
# Pitching: CWS #40 Reynaldo López
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.out("F7")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("b c s s")
b1.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("c f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 6. CWS #38 Omar Narváez (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)
t2.advance(2, "22 1B")
t2.advance(3, "32 FC5-4")

# 7. CWS #7  Tim Anderson (X - X - 38)
t2.new_ab()
t2.pitch_list("c f b b s")
t2.out("K")

# 8. CWS #22 Charles Tilson (X - X - 38)
t2.new_ab()
t2.pitch_list("c f")
t2.hit(1)
t2.thrown_out(2, "32 FC5-4", 2, 22)

# 9. CWS #32 Trayce Thompson (X - 38 - 22)
t2.new_ab(is_risp=True)
t2.pitch_list("b f d b")
t2.reach("FC5-4")

# 1. CWS #10 Yoán Moncada (38 - X - 32)
t2.new_ab(is_risp=True)
t2.out("G6-3")


# Bot 2nd
# Pitching: CWS #40 Reynaldo López
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)
b2.advance(4, "11 1B")

# 5. BOS #11 Rafael Devers (X - 28 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b f")
b2.hit(1, rbis=1)
b2.advance(2, "12 G4-3")
b2.advance(3, "19 SB")
b2.thrown_out(4, "19 FC3-2", 2, 40)

# 6. BOS #12 Brock Holt (X - X - 11)
b2.new_ab()
b2.out("G4-3")

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b b d")
b2.reach("FC3-2")
b2.advance(2, "23 SB")

# 8. BOS #23 Blake Swihart (X - X - 19)
b2.new_ab(is_risp=True)
b2.pitch_list("1 c b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 2. CWS #5  Yolmer Sánchez (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("F7")

# 3. CWS #79 José Abreu (X - X - X)
t3.new_ab()
t3.pitch_list("s f b b b f f f b")
t3.reach("BB")
t3.error(5)
t3.advance(2, "18 FC4")
t3.advance(3, "18 E5")
t3.advance("U", "7 BB")

# 4. CWS #18 Daniel Palka (X - X - 79)
t3.new_ab()
t3.pitch_list("f s f")
t3.reach("FC4")
t3.advance(2, "24 HBP")
t3.advance(3, "7 BB")

# 5. CWS #24 Matt Davidson (79 - X - 18)
t3.new_ab(is_risp=True)
t3.reach("HBP")
t3.advance(2, "7 BB")

# 6. CWS #38 Omar Narváez (79 - 18 - 24)
t3.new_ab(is_risp=True)
t3.out("IF6")

# 7. CWS #7  Tim Anderson (79 - 18 - 24)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b c b")
t3.reach("BB", rbis=1)

# 8. CWS #22 Charles Tilson (18 - 24 - 7)
t3.new_ab(is_risp=True)
t3.pitch_list("c d c")
t3.out("P6")


# Bot 3rd
# Pitching: CWS #40 Reynaldo López
b3 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b f b b")
b3.reach("BB")
b3.advance(2, "2 G5-3")
b3.thrown_out(3, "28 FC5", 3, 40)

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b3.new_ab()
b3.pitch_list("f")
b3.out("G5-3")

# 3. BOS #18 Mitch Moreland (X - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "28 FC5")

# 4. BOS #28 J.D. Martinez (X - 16 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("f f b b f f")
b3.reach("FC5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 9. CWS #32 Trayce Thompson (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("F7")

# 1. CWS #10 Yoán Moncada (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("F8")

# 2. CWS #5  Yolmer Sánchez (X - X - X)
t4.new_ab()
t4.pitch_list("c f f b c")
t4.out("!K")


# Bot 4th
# Pitching: CWS #40 Reynaldo López
b4 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("f s b b c")
b4.out("!K")

# 6. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b c f s")
b4.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 3. CWS #79 José Abreu (X - X - X)
t5.new_ab()
t5.pitch_list("c s")
t5.out("L8")

# 4. CWS #18 Daniel Palka (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(2)

# 5. CWS #24 Matt Davidson (X - 18 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("f f d s")
t5.out("K")

# 6. CWS #38 Omar Narváez (X - 18 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.out("G6-3")


# Bot 5th
# Pitching: CWS #40 Reynaldo López
b5 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.out("F9")

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(2)
b5.advance(3, "16 G4-3")

# 1. BOS #16 Andrew Benintendi (X - 3 - X)
b5.new_ab(is_risp=True)
b5.out("G4-3")

# 2. BOS #2  Xander Bogaerts (3 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d f f")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 7. CWS #7  Tim Anderson (X - X - X)
t6.new_ab()
t6.pitch_list("c s b b f b b")
t6.reach("BB")
t6.advance(2, "22 SAC5-3")
t6.advance(4, "32 G3-1")

# 8. CWS #22 Charles Tilson (X - X - 7)
t6.new_ab()
t6.out("SAC5-3")

# 9. CWS #32 Trayce Thompson (X - 7 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c t b f d")
t6.out("G3-1", rbis=1)

# 1. CWS #10 Yoán Moncada (X - X - X)
t6.new_ab()
t6.pitch_list("f f b b b c")
t6.out("!K")


# Bot 6th
# Pitching: CWS #40 Reynaldo López
b6 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)
b6.thrown_out(2, "28 DP5-4-3", 1, 40)

# 4. BOS #28 J.D. Martinez (X - X - 18)
b6.new_ab()
b6.pitch_list("s c f")
b6.out("DP5-4-3")

# 5. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(2, "12 1B")
b6.advance(3, "19 HBP")

# 6. BOS #12 Brock Holt (X - X - 11)
b6.new_ab()
b6.pitch_list("b b c b f")
b6.hit(1)
b6.advance(2, "19 HBP")

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - 12)
b6.new_ab(is_risp=True)
b6.reach("HBP")

# 8. BOS #23 Blake Swihart (11 - 12 - 19)
b6.new_ab(is_risp=True)
b6.pitch_list("f")
b6.out("P6")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
t7.pitching_substitution(37)

# 2. CWS #5  Yolmer Sánchez (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("P6")

# 3. CWS #79 José Abreu (X - X - X)
t7.new_ab()
t7.pitch_list("c b b f f f f s")
t7.out("K")

# 4. CWS #18 Daniel Palka (X - X - X)
t7.new_ab()
t7.pitch_list("f b c b b c")
t7.out("!K")


# Bot 7th
# Pitching: CWS #40 Reynaldo López
b7 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("c f f b s")
b7.out("K2-3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)
b7.advance(3, "28 BB")
b7.advance("U", "36 E4")

# Pitching change (CWS): #65 Nate Jones replaces #40 Reynaldo López
b7.pitching_substitution(65)

# 2. BOS #2  Xander Bogaerts (X - 16 - X)
b7.new_ab(is_risp=True)
b7.reach("HBP")
b7.advance(2, "28 BB")
b7.advance(3, "36 E4")

# 3. BOS #18 Mitch Moreland (X - 16 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("d")
b7.out("L8")

# 4. BOS #28 J.D. Martinez (X - 16 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("b b d b")
b7.reach("BB")
b7.advance(2, "36 E4")

# Pitching change (CWS): #57 Jace Fry replaces #65 Nate Jones
b7.pitching_substitution(57)

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #11 Rafael Devers, batting 5th
b7.offensive_substitution(5, 36, "PH")

# 5. BOS #36 Eduardo Núñez (16 - 2 - 28)
b7.new_ab(is_risp=True)
b7.pitch_list("b f")
b7.error(4)
b7.reach("E4")

# 6. BOS #12 Brock Holt (2 - 28 - 36)
b7.new_ab(is_risp=True)
b7.pitch_list("b c f d")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #44 Brandon Workman
t8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree
t8.pitching_substitution(44)

# Defensive switch (BOS): #36 Eduardo Núñez moves to 3B
t8.defensive_switch(36, "5")

# 5. CWS #24 Matt Davidson (X - X - X)
t8.new_ab()
t8.pitch_list("s b f f b t")
t8.out("KT")

# 6. CWS #38 Omar Narváez (X - X - X)
t8.new_ab()
t8.pitch_list("c f b")
t8.hit(1)

# 7. CWS #7  Tim Anderson (X - X - 38)
t8.new_ab()
t8.pitch_list("f b d f b c")
t8.out("!K")

# 8. CWS #22 Charles Tilson (X - X - 38)
t8.new_ab()
t8.pitch_list("b b b c f c")
t8.out("!K")


# Bot 8th
# Pitching: CWS #57 Jace Fry
b8 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("f c")
b8.out("G4-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("s b")
b8.hit(1)

# 9. BOS #3  Sandy León (X - X - 23)
b8.new_ab()
b8.pitch_list("c s s")
b8.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - 23)
b8.new_ab()
b8.pitch_list("1 1 c")
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Matt Barnes
t9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #44 Brandon Workman
t9.pitching_substitution(32)

# 9. CWS #32 Trayce Thompson (X - X - X)
t9.new_ab()
t9.pitch_list("b b s s s")
t9.out("K")

# 1. CWS #10 Yoán Moncada (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "5 G1-3")
t9.advance(4, "18 E6")

# 2. CWS #5  Yolmer Sánchez (X - X - 10)
t9.new_ab()
t9.pitch_list("b c b 1 1")
t9.out("G1-3")

# 3. CWS #79 José Abreu (X - 10 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("v v v v")
t9.reach("IBB")
t9.advance(4, "18 E6")

# 4. CWS #18 Daniel Palka (X - 10 - 79)
t9.new_ab(is_risp=True)
t9.pitch_list("s f")
t9.hit(2, rbis=2)
t9.error(6)
t9.advance(3, "E6")

# 5. CWS #24 Matt Davidson (18 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f s d s")
t9.out("K2-3")


# Bot 9th
# Pitching: CWS #48 Joakim Soria
b9 = game.new_inning()

# Pitching change (CWS): #48 Joakim Soria replaces #57 Jace Fry
b9.pitching_substitution(48)

# 2. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c b c b")
b9.out("G5-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b9.new_ab()
b9.pitch_list("f b s b b f b")
b9.reach("BB")
b9.advance(2, "36 DI")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b9.new_ab()
b9.pitch_list("s f b d s")
b9.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - 18)
b9.new_ab(is_risp=True)
b9.pitch_list("c f s")
b9.out("K")

# Winning team: CWS
# WP: CWS #40 Reynaldo López
game.winning_pitcher(40, is_away_team=True)
# SV: CWS #48 Joakim Soria
game.save_pitcher(48, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
