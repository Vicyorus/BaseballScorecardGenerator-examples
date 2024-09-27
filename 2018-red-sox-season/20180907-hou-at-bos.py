import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2018-09-07
# https://www.baseball-reference.com/boxes/BOS/BOS201809070.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2018/09/07/531514/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-07 19:10-22:48",
        "at": "Fenway Park, Boston, MA",
        "att": "36,930",
        "temp": "68F, Cloudy",
        "wind": "6mph, In From RF",
        "away": {
            "team": "Houston Astros",
            "starter": 45,
            "roster": {
                # Lineup
                4: "George Springer",
                27: "Jose Altuve",
                2: "Alex Bregman",
                1: "Carlos Correa",
                13: "Tyler White",
                10: "Yuli Gurriel",
                22: "Josh Reddick",
                15: "Martín Maldonado",
                6: "Jake Marisnick",
                # Starting pitcher
                45: "Gerrit Cole",
                # Bench
                11: "Evan Gattis",
                18: "Tony Kemp",
                9: "Marwin Gonzalez",
                16: "Brian McCann",
                28: "J.D. Davis",
                12: "Max Stassi",
                # Bullpen
                65: "Framber Valdez",
                30: "Héctor Rondón",
                36: "Will Harris",
                47: "Chris Devenski",
                31: "Collin McHugh",
                59: "Cionel Pérez",
                54: "Roberto Osuna",
                38: "Joe Smith",
                55: "Ryan Pressly",
                29: "Tony Sipp",
                60: "Dallas Keuchel",
                41: "Brad Peacock",
                67: "Dean Deetz",
                35: "Justin Verlander",
                63: "Josh James",
            },
            "lefties": [65, 59, 29, 60],
            "lineup": [
                [4, "9"],
                [27, "4"],
                [2, "5"],
                [1, "6"],
                [13, "0"],
                [10, "3"],
                [22, "7"],
                [15, "2"],
                [6, "8"],
            ],
            "bench": [
                [11, "DH"],
                [18, "2B"],
                [9, "SS"],
                [16, "C"],
                [28, "1B"],
                [12, "C"],
            ],
            "bullpen": [65, 30, 36, 47, 31, 59, 54, 38, 55, 29, 60, 41, 67, 35, 63],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 31, 61, 66, 63],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "James Hoye",
            "2B": "David Rackley",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
t1.new_ab()
t1.out("P4")

# 2. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("c b b s c")
t1.out("!K")

# 3. HOU #2  Alex Bregman (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b b")
t1.reach("BB")

# 4. HOU #1  Carlos Correa (X - X - 2)
t1.new_ab()
t1.pitch_list("b c b b f c")
t1.out("!K")


# Bot 1st
# Pitching: HOU #45 Gerrit Cole
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.advance(3, "16 1B")
b1.advance(4, "28 SF9")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b 1 b f b")
b1.hit(1)
b1.thrown_out(2, "2 CS", 3, 45)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b1.new_ab()
b1.out("SF9", rbis=1)

# 4. BOS #2  Xander Bogaerts (X - X - 16)
b1.new_ab()
b1.pitch_list("1 b c s d s")
b1.out("KDP2-6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 5. HOU #13 Tyler White (X - X - X)
t2.new_ab()
t2.pitch_list("b b c c b f s")
t2.out("K")

# 6. HOU #10 Yuli Gurriel (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.thrown_out(2, "15 FC4", 3, 24)

# 7. HOU #22 Josh Reddick (X - X - 10)
t2.new_ab()
t2.pitch_list("b b f s f s")
t2.out("K")

# 8. HOU #15 Martín Maldonado (X - X - 10)
t2.new_ab()
t2.pitch_list("b c s b")
t2.reach("FC4")


# Bot 2nd
# Pitching: HOU #45 Gerrit Cole
b2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b c f s")
b2.out("K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("P6")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 9. HOU #6  Jake Marisnick (X - X - X)
t3.new_ab()
t3.out("L7")

# 1. HOU #4  George Springer (X - X - X)
t3.new_ab()
t3.pitch_list("b c t c")
t3.out("!K")

# 2. HOU #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c s c")
t3.out("!K")


# Bot 3rd
# Pitching: HOU #45 Gerrit Cole
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b f s")
b3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b s b b b")
b3.reach("BB")
b3.advance(2, "50 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("c b 1 f")
b3.hit(1)

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b3.new_ab()
b3.pitch_list("b")
b3.out("L7")

# 3. BOS #28 J.D. Martinez (X - 19 - 50)
b3.new_ab()
b3.pitch_list("f s f b d s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 3. HOU #2  Alex Bregman (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b")
t4.out("P4")

# 4. HOU #1  Carlos Correa (X - X - X)
t4.new_ab()
t4.pitch_list("b f c f b f")
t4.out("F8")

# 5. HOU #13 Tyler White (X - X - X)
t4.new_ab()
t4.pitch_list("c b b c c")
t4.out("!K")


# Bot 4th
# Pitching: HOU #45 Gerrit Cole
b4 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c c b f f")
b4.hit(4)

# 5. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("G3")

# 6. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.out("L9")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b f")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 6. HOU #10 Yuli Gurriel (X - X - X)
t5.new_ab()
t5.out("L9")

# 7. HOU #22 Josh Reddick (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F7")

# 8. HOU #15 Martín Maldonado (X - X - X)
t5.new_ab()
t5.pitch_list("c b s b s")
t5.out("K")


# Bot 5th
# Pitching: HOU #45 Gerrit Cole
b5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("f b c s")
b5.wp()
b5.reach("K")
b5.advance(2, "50 1B")
b5.advance(3, "28 BB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b5.new_ab()
b5.pitch_list("s c s")
b5.out("K")

# 1. BOS #50 Mookie Betts (X - X - 3)
b5.new_ab()
b5.pitch_list("b c b")
b5.hit(1)
b5.advance(2, "28 BB")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
b5.new_ab()
b5.out("L7")

# 3. BOS #28 J.D. Martinez (X - 3 - 50)
b5.new_ab()
b5.pitch_list("d s b b b")
b5.reach("BB")

# 4. BOS #2  Xander Bogaerts (3 - 50 - 28)
b5.new_ab()
b5.pitch_list("f d c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 9. HOU #6  Jake Marisnick (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("(F)P3")

# 1. HOU #4  George Springer (X - X - X)
t6.new_ab()
t6.pitch_list("f f b f b c")
t6.out("!K")

# 2. HOU #27 Jose Altuve (X - X - X)
t6.new_ab()
t6.pitch_list("f t b b")
t6.out("G5-3")


# Bot 6th
# Pitching: HOU #45 Gerrit Cole
b6 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("G6-3")

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f f f f b c")
b6.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("L8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 3. HOU #2  Alex Bregman (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(2)
t7.advance(4, "10 2B")

# 4. HOU #1  Carlos Correa (X - 2 - X)
t7.new_ab()
t7.pitch_list("b c b b f c")
t7.out("!K")

# 5. HOU #13 Tyler White (X - 2 - X)
t7.new_ab()
t7.pitch_list("f b b b s b")
t7.reach("BB")
t7.advance(3, "10 2B")
t7.advance(4, "18 2B")

# Pitching change (BOS): #70 Ryan Brasier replaces #24 David Price
t7.pitching_substitution(70)

# 6. HOU #10 Yuli Gurriel (X - 2 - 13)
t7.new_ab()
t7.hit(2, rbis=1)
t7.advance(4, "18 2B")

# 7. HOU #22 Josh Reddick (13 - 10 - X)
t7.new_ab()
t7.out("(F)P2")

# Offensive change (HOU): Pinch-hitter #18 Tony Kemp replaces #15 Martín Maldonado, batting 8th
t7.offensive_substitution(8, 18, "PH")

# 8. HOU #18 Tony Kemp (13 - 10 - X)
t7.new_ab()
t7.pitch_list("d d b c c")
t7.hit(2, rbis=2)

# 9. HOU #6  Jake Marisnick (X - 18 - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("G6-3")


# Bot 7th
# Pitching: HOU #31 Collin McHugh
b7 = game.new_inning()

# Pitching change (HOU): #31 Collin McHugh replaces #45 Gerrit Cole
b7.pitching_substitution(31)

# Defensive change (HOU): #16 Brian McCann replaces #18 Tony Kemp (PH), playing C, batting 8th
b7.defensive_substitution(8, 16, "2")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #3 Sandy León, batting 8th
b7.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c b f s")
b7.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b b f s b f f b")
b7.reach("BB")
b7.advance(2, "50 WP")
b7.advance(3, "16 FC3-6")
b7.advance(4, "28 1B")

# Pitching change (HOU): #55 Ryan Pressly replaces #31 Collin McHugh
b7.pitching_substitution(55)

# 1. BOS #50 Mookie Betts (X - X - 19)
b7.new_ab()
b7.pitch_list("b 1 b b b")
b7.wp()
b7.reach("BB")
b7.thrown_out(2, "16 FC3-6", 2, 55)

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b7.new_ab()
b7.pitch_list("c")
b7.reach("FC3-6")
b7.advance(3, "28 1B")

# 3. BOS #28 J.D. Martinez (19 - X - 16)
b7.new_ab()
b7.pitch_list("s")
b7.hit(1, rbis=1)

# 4. BOS #2  Xander Bogaerts (16 - X - 28)
b7.new_ab()
b7.pitch_list("b c s b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #70 Ryan Brasier
t8.pitching_substitution(56)

# Defensive change (BOS): #7 Christian Vázquez replaces #12 Brock Holt (PH), playing C, batting 8th
t8.defensive_substitution(8, 7, "2")

# 1. HOU #4  George Springer (X - X - X)
t8.new_ab()
t8.pitch_list("b s s b b f")
t8.hit(1)
t8.advance(2, "27 1B")
t8.advance(3, "2 1B")
t8.advance(4, "1 SF9")

# 2. HOU #27 Jose Altuve (X - X - 4)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(1)
t8.advance(2, "2 1B")
t8.advance(3, "1 SF9")
t8.advance(4, "13 WP")

# 3. HOU #2  Alex Bregman (X - 4 - 27)
t8.new_ab()
t8.hit(1)
t8.advance(2, "1 SF9")
t8.advance(3, "13 WP")
t8.advance(4, "13 1B")

# 4. HOU #1  Carlos Correa (4 - 27 - 2)
t8.new_ab()
t8.pitch_list("b")
t8.out("SF9", rbis=1)

# 5. HOU #13 Tyler White (27 - 2 - X)
t8.new_ab()
t8.pitch_list("c b f f b")
t8.wp()
t8.hit(1, rbis=1)

# 6. HOU #10 Yuli Gurriel (X - X - 13)
t8.new_ab()
t8.pitch_list("c b b b c s")
t8.out("K")

# 7. HOU #22 Josh Reddick (X - X - 13)
t8.new_ab()
t8.pitch_list("c d")
t8.out("F8")


# Bot 8th
# Pitching: HOU #30 Héctor Rondón
b8 = game.new_inning()

# Pitching change (HOU): #30 Héctor Rondón replaces #55 Ryan Pressly
b8.pitching_substitution(30)

# 5. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c s b s")
b8.out("K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)
b8.advance(2, "36 1B")

# 7. BOS #36 Eduardo Núñez (X - X - 5)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)

# Offensive change (BOS): Pinch-hitter #11 Rafael Devers replaces #7 Christian Vázquez, batting 8th
b8.offensive_substitution(8, 11, "PH")

# 8. BOS #11 Rafael Devers (X - 5 - 36)
b8.new_ab()
b8.pitch_list("c f f b s")
b8.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - 5 - 36)
b8.new_ab()
b8.pitch_list("b s")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #56 Joe Kelly
t9.pitching_substitution(47)

# Defensive change (BOS): #23 Blake Swihart replaces #11 Rafael Devers (PH), playing C, batting 8th
t9.defensive_substitution(8, 23, "2")

# 8. HOU #16 Brian McCann (X - X - X)
t9.new_ab()
t9.pitch_list("b c c f")
t9.hit(1)
t9.advance(2, "4 1B")
t9.thrown_out(3, "27 DP5-3", 2, 47)

# 9. HOU #6  Jake Marisnick (X - X - 16)
t9.new_ab()
t9.pitch_list("f c s")
t9.out("K")

# 1. HOU #4  George Springer (X - X - 16)
t9.new_ab()
t9.hit(1)

# 2. HOU #27 Jose Altuve (X - 16 - 4)
t9.new_ab()
t9.pitch_list("d d f")
t9.out("DP5-3")


# Bot 9th
# Pitching: HOU #54 Roberto Osuna
b9 = game.new_inning()

# Pitching change (HOU): #54 Roberto Osuna replaces #30 Héctor Rondón
b9.pitching_substitution(54)

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("c s b b")
b9.out("L7")

# 3. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("f b")
b9.out("G5-3")

# Winning team: HOU
# WP: HOU #55 Ryan Pressly
game.winning_pitcher(55, is_away_team=True)
# SV: HOU #54 Roberto Osuna
game.save_pitcher(54, is_away_team=True)

# Loser team: BOS
# LP: BOS #56 Joe Kelly
game.losing_pitcher(56)

# print(game)
game.generate_scorecard()
