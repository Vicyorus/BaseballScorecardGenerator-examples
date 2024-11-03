import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2018-09-08
# https://www.baseball-reference.com/boxes/BOS/BOS201809080.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2018/09/08/531529/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-08 16:06-19:31",
        "at": "Fenway Park, Boston, MA",
        "att": "36,684",
        "temp": "67F, Partly Cloudy",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Houston Astros",
            "starter": 50,
            "roster": {
                # Lineup
                4: "George Springer",
                27: "Jose Altuve",
                2: "Alex Bregman",
                10: "Yuli Gurriel",
                1: "Carlos Correa",
                13: "Tyler White",
                6: "Jake Marisnick",
                15: "Martín Maldonado",
                18: "Tony Kemp",
                # Starting pitcher
                50: "Charlie Morton",
                # Bench
                11: "Evan Gattis",
                22: "Josh Reddick",
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
                45: "Gerrit Cole",
                67: "Dean Deetz",
                35: "Justin Verlander",
                63: "Josh James",
            },
            "lefties": [65, 59, 29, 60],
            "lineup": [
                [4, "9"],
                [27, "4"],
                [2, "5"],
                [10, "3"],
                [1, "6"],
                [13, "0"],
                [6, "8"],
                [15, "2"],
                [18, "7"],
            ],
            "bench": [
                [11, "DH"],
                [22, "RF"],
                [9, "SS"],
                [16, "C"],
                [28, "1B"],
                [12, "C"],
            ],
            "bullpen": [65, 30, 36, 47, 31, 59, 54, 38, 55, 29, 60, 41, 45, 67, 35, 63],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                59: "Sam Travis",
                23: "Blake Swihart",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [12, "2B"],
                [59, "1B"],
                [23, "C"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "David Rackley",
            "1B": "Quinn Wolcott",
            "2B": "Paul Nauert",
            "3B": "James Hoye",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
t1.new_ab()
t1.pitch_list("b b f c f c")
t1.out("!K")

# 2. HOU #27 Jose Altuve (X - X - X)
t1.new_ab()
t1.pitch_list("c b c s")
t1.out("K")

# 3. HOU #2  Alex Bregman (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("L4")


# Bot 1st
# Pitching: HOU #50 Charlie Morton
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b b f f")
b1.hit(1)
b1.advance(2, "16 1B")
b1.advance(3, "28 L8")
b1.advance(4, "2 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("f d 1")
b1.hit(1)
b1.advance(2, "2 1B")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("L8")

# 4. BOS #2  Xander Bogaerts (50 - X - 16)
b1.new_ab(is_risp=True)
b1.hit(1, rbis=1)

# 5. BOS #18 Mitch Moreland (X - 16 - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("L9")

# 6. BOS #5  Ian Kinsler (X - 16 - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 4. HOU #10 Yuli Gurriel (X - X - X)
t2.new_ab()
t2.pitch_list("f c f c")
t2.out("!K")

# 5. HOU #1  Carlos Correa (X - X - X)
t2.new_ab()
t2.pitch_list("s b")
t2.hit(2)
t2.advance(4, "13 3B")

# 6. HOU #13 Tyler White (X - 1 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.hit(3, rbis=1)
t2.advance(4, "6 SF8")

# 7. HOU #6  Jake Marisnick (13 - X - X)
t2.new_ab(is_risp=True)
t2.pitch_list("f f")
t2.out("SF8", rbis=1)

# 8. HOU #15 Martín Maldonado (X - X - X)
t2.new_ab()
t2.pitch_list("f b c b f b b")
t2.reach("BB")
t2.advance(2, "18 1B")

# 9. HOU #18 Tony Kemp (X - X - 15)
t2.new_ab()
t2.pitch_list("b f f")
t2.hit(1)

# 1. HOU #4  George Springer (X - 15 - 18)
t2.new_ab(is_risp=True)
t2.pitch_list("s")
t2.out("F9")


# Bot 2nd
# Pitching: HOU #50 Charlie Morton
b2 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("c f f s")
b2.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b f f")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 2. HOU #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("f b b b")
t3.out("L8")

# 3. HOU #2  Alex Bregman (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(4)

# 4. HOU #10 Yuli Gurriel (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.advance(2, "13 BB")

# 5. HOU #1  Carlos Correa (X - X - 10)
t3.new_ab()
t3.pitch_list("c b c b f f f s")
t3.out("K")

# 6. HOU #13 Tyler White (X - X - 10)
t3.new_ab()
t3.pitch_list("f f b b b 1 f f b")
t3.reach("BB")

# 7. HOU #6  Jake Marisnick (X - 10 - 13)
t3.new_ab(is_risp=True)
t3.pitch_list("f b")
t3.out("P4")


# Bot 3rd
# Pitching: HOU #50 Charlie Morton
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.hit(2)
b3.advance(3, "2 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b c")
b3.out("L8")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f")
b3.out("G6-3")

# 4. BOS #2  Xander Bogaerts (X - 50 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c s f b")
b3.hit(1)

# 5. BOS #18 Mitch Moreland (50 - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("c b s f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 8. HOU #15 Martín Maldonado (X - X - X)
t4.new_ab()
t4.pitch_list("f b b c")
t4.hit(4)

# 9. HOU #18 Tony Kemp (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")

# 1. HOU #4  George Springer (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b b")
t4.reach("BB")
t4.advance(3, "27 1B")
t4.advance(4, "10 SF9")

# Pitching change (BOS): #44 Brandon Workman replaces #57 Eduardo Rodriguez
t4.pitching_substitution(44)

# 2. HOU #27 Jose Altuve (X - X - 4)
t4.new_ab()
t4.hit(1)
t4.advance(2, "2 BB")

# 3. HOU #2  Alex Bregman (4 - X - 27)
t4.new_ab(is_risp=True)
t4.pitch_list("1 b f b d c b")
t4.reach("BB")
t4.thrown_out(2, "1 FC6-4", 3, 44)

# 4. HOU #10 Yuli Gurriel (4 - 27 - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("SF9", rbis=1)

# 5. HOU #1  Carlos Correa (X - 27 - 2)
t4.new_ab(is_risp=True)
t4.reach("FC6-4")


# Bot 4th
# Pitching: HOU #50 Charlie Morton
b4 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.pitch_list("c f")
b4.out("G6-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b f")
b4.out("G6-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("f b b b b")
b4.reach("BB")
b4.advance(2, "19 1B")
b4.advance(3, "50 BB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.advance(2, "50 BB")

# 1. BOS #50 Mookie Betts (X - 7 - 19)
b4.new_ab(is_risp=True)
b4.pitch_list("c b b b f b")
b4.reach("BB")

# 2. BOS #16 Andrew Benintendi (7 - 19 - 50)
b4.new_ab(is_risp=True)
b4.pitch_list("b b f")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #44 Brandon Workman
t5 = game.new_inning()

# 6. HOU #13 Tyler White (X - X - X)
t5.new_ab()
t5.pitch_list("c t b b")
t5.out("G6-3")

# 7. HOU #6  Jake Marisnick (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 8. HOU #15 Martín Maldonado (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.thrown_out(2, "18 FC6-4", 3, 44)

# 9. HOU #18 Tony Kemp (X - X - 15)
t5.new_ab()
t5.pitch_list("c")
t5.reach("FC6-4")


# Bot 5th
# Pitching: HOU #50 Charlie Morton
b5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c c f")
b5.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.hit(4)

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f b s")
b5.out("K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #66 Bobby Poyner
t6 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #44 Brandon Workman
t6.pitching_substitution(66)

# 1. HOU #4  George Springer (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.hit(1)
t6.advance(2, "27 HBP")

# 2. HOU #27 Jose Altuve (X - X - 4)
t6.new_ab()
t6.pitch_list("c")
t6.reach("HBP")

# 3. HOU #2  Alex Bregman (X - 4 - 27)
t6.new_ab(is_risp=True)
t6.pitch_list("s s b f b s")
t6.out("K")

# 4. HOU #10 Yuli Gurriel (X - 4 - 27)
t6.new_ab(is_risp=True)
t6.pitch_list("s c")
t6.out("IF6")

# 5. HOU #1  Carlos Correa (X - 4 - 27)
t6.new_ab(is_risp=True)
t6.pitch_list("s s")
t6.out("G3-1")


# Bot 6th
# Pitching: HOU #63 Josh James
b6 = game.new_inning()

# Pitching change (HOU): #63 Josh James replaces #50 Charlie Morton
b6.pitching_substitution(63)

# 7. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("G6-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("(F)P3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("c f f f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #66 Bobby Poyner
t7 = game.new_inning()

# 6. HOU #13 Tyler White (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b s")
t7.out("K")

# 7. HOU #6  Jake Marisnick (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F8")

# 8. HOU #15 Martín Maldonado (X - X - X)
t7.new_ab()
t7.pitch_list("s c s")
t7.out("K")


# Bot 7th
# Pitching: HOU #63 Josh James
b7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c b c b s")
b7.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #47 Tyler Thornburg
t8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #66 Bobby Poyner
t8.pitching_substitution(47)

# 9. HOU #18 Tony Kemp (X - X - X)
t8.new_ab()
t8.pitch_list("c c")
t8.hit(1)
t8.error(5)
t8.advance(2, "4 1B")
t8.advance(3, "4 E5")

# 1. HOU #4  George Springer (X - X - 18)
t8.new_ab()
t8.hit(1)
t8.advance(2, "E5")

# 2. HOU #27 Jose Altuve (18 - 4 - X)
t8.new_ab(is_risp=True)
t8.out("F7")

# 3. HOU #2  Alex Bregman (18 - 4 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("d c f s")
t8.out("K")

# 4. HOU #10 Yuli Gurriel (18 - 4 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("d")
t8.out("P4")


# Bot 8th
# Pitching: HOU #63 Josh James
b8 = game.new_inning()

# Defensive change (HOU): #22 Josh Reddick replaces #18 Tony Kemp (LF), playing LF, batting 9th
b8.defensive_substitution(9, 22, "7")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("f f s")
b8.out("K")

# 5. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c s f f")
b8.hit(2)

# 6. BOS #5  Ian Kinsler (X - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b b c b f f c")
b8.out("!K")

# Pitching change (HOU): #55 Ryan Pressly replaces #63 Josh James
b8.pitching_substitution(55)

# 7. BOS #11 Rafael Devers (X - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c c c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# 5. HOU #1  Carlos Correa (X - X - X)
t9.new_ab()
t9.pitch_list("c b b s")
t9.out("L3")

# 6. HOU #13 Tyler White (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b b")
t9.reach("BB")
# Offensive change (HOU): Pinch-runner #9 Marwin Gonzalez replaces #13 Tyler White
t9.offensive_substitution(6, 9, "PR")
t9.atbase("PR")
t9.thrown_out(2, "6 DP5-4-3", 2, 47)

# 7. HOU #6  Jake Marisnick (X - X - 13)
t9.new_ab()
t9.out("DP5-4-3")


# Bot 9th
# Pitching: HOU #54 Roberto Osuna
b9 = game.new_inning()

# Pitching change (HOU): #54 Roberto Osuna replaces #55 Ryan Pressly
b9.pitching_substitution(54)

# Defensive switch (HOU): #9 Marwin Gonzalez moves to DH
b9.defensive_switch(9, "0")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #7 Christian Vázquez, batting 8th
b9.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Blake Swihart (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(2, "50 BB")
b9.advance(3, "16 WP")
b9.advance(4, "16 1B")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
b9.new_ab()
b9.out("P3")

# 1. BOS #50 Mookie Betts (X - X - 23)
b9.new_ab()
b9.pitch_list("b c b b d")
b9.reach("BB")
b9.advance(2, "16 WP")
b9.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 23 - 50)
b9.new_ab(is_risp=True)
b9.pitch_list("c b s")
b9.wp()
b9.hit(1, rbis=1)
b9.thrown_out(2, "28 DP6-4-3", 2, 54)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b9.new_ab(is_risp=True)
b9.pitch_list("f f")
b9.out("DP6-4-3")

# Winning team: HOU
# WP: HOU #50 Charlie Morton
game.winning_pitcher(50, is_away_team=True)
# SV: HOU #54 Roberto Osuna
game.save_pitcher(54, is_away_team=True)

# Loser team: BOS
# LP: BOS #57 Eduardo Rodriguez
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
