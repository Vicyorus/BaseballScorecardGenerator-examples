import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-05-11
# https://www.baseball-reference.com/boxes/TOR/TOR201805110.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/05/11/529973/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-11 19:08-23:02",
        "at": "Rogers Centre, Toronto, ON",
        "att": "28,695",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                11: "Rafael Devers",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
            ],
            "bench": [
                [11, "3B"],
                [23, "C"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 22, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 41,
            "roster": {
                # Lineup
                37: "Teoscar Hernández",
                20: "Josh Donaldson",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                11: "Kevin Pillar",
                8: "Kendrys Morales",
                30: "Anthony Alford",
                21: "Luke Maile",
                13: "Lourdes Gurriel Jr.",
                # Starting pitcher
                41: "Aaron Sanchez",
                # Bench
                55: "Russell Martin",
                7: "Richard Urena",
                23: "Dalton Pompey",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                31: "Joe Biagini",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                77: "John Axford",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 33],
            "lineup": [
                [37, "9"],
                [20, "5"],
                [26, "4"],
                [14, "3"],
                [11, "8"],
                [8, "0"],
                [30, "7"],
                [21, "2"],
                [13, "6"],
            ],
            "bench": [
                [55, "C"],
                [7, "SS"],
                [23, "CF"],
                [18, "CF"],
            ],
            "bullpen": [62, 57, 31, 25, 39, 43, 36, 22, 77, 52, 33],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Ron Kulpa",
            "2B": "Jerry Meals",
            "3B": "Gabe Morales",
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
# Pitching: TOR #41 Aaron Sanchez
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b b")
t1.reach("BB")
t1.advance(3, "16 1B")
t1.advance(4, "28 G3")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("f s b 1 b f f 1 b")
t1.hit(1)
t1.advance(2, "28 SB")
t1.advance(3, "28 G3")

# 3. BOS #13 Hanley Ramirez (50 - X - 16)
t1.new_ab()
t1.pitch_list("s s c")
t1.out("!K")

# 4. BOS #28 J.D. Martinez (50 - X - 16)
t1.new_ab()
t1.pitch_list("c s f b b f")
t1.out("G3", rbis=1)

# 5. BOS #2  Xander Bogaerts (16 - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
b1.new_ab()
b1.hit(2)
b1.advance(4, "20 1B")

# 2. TOR #20 Josh Donaldson (X - 37 - X)
b1.new_ab()
b1.pitch_list("b s")
b1.hit(1, rbis=1)

# 3. TOR #26 Yangervis Solarte (X - X - 20)
b1.new_ab()
b1.pitch_list("s f f f 1 f s 1")
b1.out("K")

# 4. TOR #14 Justin Smoak (X - X - 20)
b1.new_ab()
b1.pitch_list("c b b c s 1")
b1.out("K")

# 5. TOR #11 Kevin Pillar (X - X - 20)
b1.new_ab()
b1.pitch_list("b c s")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #41 Aaron Sanchez
t2 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b b t")
t2.out("G1-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(1)

# 8. BOS #12 Brock Holt (X - X - 36)
t2.new_ab()
t2.pitch_list("c s b")
t2.out("P6")

# 9. BOS #3  Sandy León (X - X - 36)
t2.new_ab()
t2.pitch_list("b b f c f")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 6. TOR #8  Kendrys Morales (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(2)
b2.advance(3, "30 F9")
b2.advance(4, "21 1B")

# 7. TOR #30 Anthony Alford (X - 8 - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 8. TOR #21 Luke Maile (8 - X - X)
b2.new_ab()
b2.pitch_list("d")
b2.hit(1, rbis=1)
b2.advance(2, "37 E1")

# 9. TOR #13 Lourdes Gurriel Jr. (X - X - 21)
b2.new_ab()
b2.pitch_list("c f t")
b2.out("KT")

# 1. TOR #37 Teoscar Hernández (X - X - 21)
b2.new_ab()
b2.pitch_list("b b")
b2.error(1)
b2.reach("E1")

# 2. TOR #20 Josh Donaldson (X - 21 - 37)
b2.new_ab()
b2.pitch_list("b s b c f b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #41 Aaron Sanchez
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c c s")
t3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.out("G3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("b f s b f b f d")
t3.reach("BB")
t3.thrown_out(4, "28 8-6-2", 3, 41)
t3.advance(3, "28 2B")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t3.new_ab()
t3.pitch_list("d f b")
t3.hit(2)


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G6-3")

# 4. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G3-1")

# 5. TOR #11 Kevin Pillar (X - X - X)
b3.new_ab()
b3.pitch_list("c s")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #41 Aaron Sanchez
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4)

# 6. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("t b s f f f b")
t4.hit(1)
t4.thrown_out(2, "36 FC6-4", 1, 41)

# 7. BOS #36 Eduardo Núñez (X - X - 18)
t4.new_ab()
t4.pitch_list("f f")
t4.reach("FC6-4")
t4.thrown_out(2, "12 FC4-6", 2, 41)

# 8. BOS #12 Brock Holt (X - X - 36)
t4.new_ab()
t4.reach("FC4-6")
t4.advance("U", "3 PB")

# 9. BOS #3  Sandy León (X - X - 12)
t4.new_ab()
t4.pitch_list("f f b s")
t4.pb()
t4.reach("K")
t4.error(2)
t4.advance(3, "E2")

# 1. BOS #50 Mookie Betts (3 - X - X)
t4.new_ab()
t4.out("L7")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 6. TOR #8  Kendrys Morales (X - X - X)
b4.new_ab()
b4.pitch_list("c s b s")
b4.out("K")

# 7. TOR #30 Anthony Alford (X - X - X)
b4.new_ab()
b4.pitch_list("c f b s")
b4.out("K")

# 8. TOR #21 Luke Maile (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #41 Aaron Sanchez
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("b f b b b")
t5.reach("BB")
t5.advance(2, "28 F8")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t5.new_ab()
t5.pitch_list("s 1 b f t")
t5.out("KT")

# 4. BOS #28 J.D. Martinez (X - X - 16)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 5. BOS #2  Xander Bogaerts (X - 16 - X)
t5.new_ab()
t5.pitch_list("b b c s")
t5.out("L5")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 9. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("f s b s")
b5.out("K")

# 1. TOR #37 Teoscar Hernández (X - X - X)
b5.new_ab()
b5.pitch_list("b c b c t")
b5.out("KT")

# 2. TOR #20 Josh Donaldson (X - X - X)
b5.new_ab()
b5.pitch_list("b c c b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #77 John Axford
t6 = game.new_inning()

# Pitching change (TOR): #77 John Axford replaces #41 Aaron Sanchez
t6.pitching_substitution(77)

# 6. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f b")
t6.reach("BB")
t6.thrown_out(2, "36 DP6-4-3", 1, 77)

# 7. BOS #36 Eduardo Núñez (X - X - 18)
t6.new_ab()
t6.pitch_list("b")
t6.out("DP6-4-3")

# 8. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G1-3")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
b6.new_ab()
b6.pitch_list("f f")
b6.out("P3")

# 4. TOR #14 Justin Smoak (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b c")
b6.out("!K")

# 5. TOR #11 Kevin Pillar (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("L4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #22 Seunghwan Oh
t7 = game.new_inning()

# Pitching change (TOR): #22 Seunghwan Oh replaces #77 John Axford
t7.pitching_substitution(22)

# 9. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("b c b f s")
t7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("c c b b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 6. TOR #8  Kendrys Morales (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 7. TOR #30 Anthony Alford (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("G4-3")

# 8. TOR #21 Luke Maile (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(4)

# 9. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b s b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #52 Ryan Tepera
t8 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #22 Seunghwan Oh
t8.pitching_substitution(52)

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("b b f b s c")
t8.out("!K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.out("(F)P3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f")
t8.out("(F)P2")


# Bot 8th
# Pitching: BOS #41 Chris Sale
b8 = game.new_inning()

# 1. TOR #37 Teoscar Hernández (X - X - X)
b8.new_ab()
b8.out("G3")

# 2. TOR #20 Josh Donaldson (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f s")
b8.out("K")

# 3. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #36 Tyler Clippard
t9 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #52 Ryan Tepera
t9.pitching_substitution(36)

# 6. BOS #18 Mitch Moreland (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F9")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c c f b f c")
t9.out("!K")

# 8. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c s b c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #41 Chris Sale
b9 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
b9.new_ab()
b9.pitch_list("b f f s")
b9.out("K")

# 5. TOR #11 Kevin Pillar (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.hit(2)
b9.thrown_out(3, "8-4-5", 2, 41)

# 6. TOR #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.pitch_list("b b f s f")
b9.out("G6-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TOR #43 Sam Gaviglio
t10 = game.new_inning()

# Pitching change (TOR): #43 Sam Gaviglio replaces #36 Tyler Clippard
t10.pitching_substitution(43)

# Offensive change (BOS): Pinch-hitter #11 Rafael Devers replaces #3 Sandy León, batting 9th
t10.offensive_substitution(9, 11, "PH")

# 9. BOS #11 Rafael Devers (X - X - X)
t10.new_ab()
t10.pitch_list("f b f f f c")
t10.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t10.new_ab()
t10.pitch_list("c b c b b")
t10.error(6)
t10.reach("E6")
t10.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t10.new_ab()
t10.pitch_list("c 1 1 f 1 b b f")
t10.out("(F)P5")

# 3. BOS #13 Hanley Ramirez (X - 50 - X)
t10.new_ab()
t10.pitch_list("b f")
t10.out("G5-3")


# Bot 10th
# Pitching: BOS #32 Matt Barnes
b10 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
b10.pitching_substitution(32)

# Defensive change (BOS): #7 Christian Vázquez replaces #11 Rafael Devers (PH), playing C, batting 9th
b10.defensive_substitution(9, 7, "2")

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #30 Anthony Alford, batting 7th
b10.offensive_substitution(7, 18, "PH")

# 7. TOR #18 Curtis Granderson (X - X - X)
b10.new_ab()
b10.pitch_list("c b b b c b")
b10.reach("BB")
b10.advance(2, "21 BB")

# 8. TOR #21 Luke Maile (X - X - 18)
b10.new_ab()
b10.pitch_list("c f 1 b b 1 b b")
b10.reach("BB")

# Offensive change (TOR): Pinch-hitter #23 Dalton Pompey replaces #13 Lourdes Gurriel Jr., batting 9th
b10.offensive_substitution(9, 23, "PH")

# 9. TOR #23 Dalton Pompey (X - 18 - 21)
b10.new_ab()
b10.pitch_list("l s l")
b10.out("K")

# 1. TOR #37 Teoscar Hernández (X - 18 - 21)
b10.new_ab()
b10.pitch_list("b f t b b")
b10.out("L9")

# 2. TOR #20 Josh Donaldson (X - 18 - 21)
b10.new_ab()
b10.pitch_list("f b s b f s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: TOR #43 Sam Gaviglio
t11 = game.new_inning()

# Defensive switch (TOR): #18 Curtis Granderson moves to LF
t11.defensive_switch(18, "7")

# Defensive change (TOR): #7 Richard Urena replaces #23 Dalton Pompey (PH), playing SS, batting 9th
t11.defensive_substitution(9, 7, "6")

# 4. BOS #28 J.D. Martinez (X - X - X)
t11.new_ab()
t11.pitch_list("b c f t")
t11.out("KT")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t11.new_ab()
t11.pitch_list("b c b")
t11.reach("HBP")

# 6. BOS #18 Mitch Moreland (X - X - 2)
t11.new_ab()
t11.pitch_list("f")
t11.out("F7")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t11.new_ab()
t11.pitch_list("d c")
t11.out("F8")


# Bot 11th
# Pitching: BOS #39 Carson Smith
b11 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #32 Matt Barnes
b11.pitching_substitution(39)

# 3. TOR #26 Yangervis Solarte (X - X - X)
b11.new_ab()
b11.pitch_list("b s c f f")
b11.out("G3")

# 4. TOR #14 Justin Smoak (X - X - X)
b11.new_ab()
b11.pitch_list("c b t b s")
b11.out("K")

# 5. TOR #11 Kevin Pillar (X - X - X)
b11.new_ab()
b11.pitch_list("c f")
b11.hit(1)
b11.advance(2, "8 SB")

# 6. TOR #8  Kendrys Morales (X - X - 11)
b11.new_ab()
b11.pitch_list("f c 1 1 b d b s")
b11.out("K")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: TOR #43 Sam Gaviglio
t12 = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
t12.new_ab()
t12.pitch_list("c")
t12.hit(1)

# 9. BOS #7  Christian Vázquez (X - X - 12)
t12.new_ab()
t12.out("F7")

# 1. BOS #50 Mookie Betts (X - X - 12)
t12.new_ab()
t12.pitch_list("c c b 1 f s")
t12.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - 12)
t12.new_ab()
t12.pitch_list("b")
t12.out("F9")


# Bot 12th
# Pitching: BOS #61 Brian Johnson
b12 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #39 Carson Smith
b12.pitching_substitution(61)

# 7. TOR #18 Curtis Granderson (X - X - X)
b12.new_ab()
b12.pitch_list("b b b b")
b12.reach("BB")
b12.advance(4, "21 HR")

# 8. TOR #21 Luke Maile (X - X - 18)
b12.new_ab()
b12.hit(4, rbis=2)

# Winning team: TOR
# WP: TOR #43 Sam Gaviglio
game.winning_pitcher(43)

# Loser team: BOS
# LP: BOS #61 Brian Johnson
game.losing_pitcher(61, is_away_team=True)

# print(game)
game.generate_scorecard()
