import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-09-20
# https://www.baseball-reference.com/boxes/NYA/NYA201809200.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/09/20/531690/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-20 19:10-23:12",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "47,351",
        "temp": "69F, Cloudy",
        "wind": "6mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                59: "Sam Travis",
                5: "Ian Kinsler",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
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
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "0"],
                [16, "7"],
                [28, "9"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [23, "3"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [18, "1B"],
                [59, "1B"],
                [5, "2B"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 19,
            "roster": {
                # Lineup
                26: "Andrew McCutchen",
                99: "Aaron Judge",
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                41: "Miguel Andujar",
                24: "Gary Sánchez",
                45: "Luke Voit",
                25: "Gleyber Torres",
                # Starting pitcher
                19: "Masahiro Tanaka",
                # Bench
                28: "Austin Romine",
                33: "Greg Bird",
                66: "Kyle Higashioka",
                29: "Adeiny Hechavarría",
                11: "Brett Gardner",
                12: "Tyler Wade",
                74: "Ronald Torreyes",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                65: "Domingo Germán",
                36: "Lance Lynn",
                43: "Chance Adams",
                38: "Jonathan Loáisiga",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                53: "Zack Britton",
                57: "Chad Green",
                48: "Tommy Kahnle",
                85: "Luis Cessa",
                71: "Stephen Tarpley",
                34: "J.A. Happ",
                30: "David Robertson",
                61: "Justus Sheffield",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 71, 34, 61, 54],
            "lineup": [
                [26, "7"],
                [99, "9"],
                [31, "8"],
                [27, "0"],
                [18, "6"],
                [41, "5"],
                [24, "2"],
                [45, "3"],
                [25, "4"],
            ],
            "bench": [
                [28, "C"],
                [33, "1B"],
                [66, "C"],
                [29, "2B"],
                [11, "LF"],
                [12, "3B"],
                [74, "SS"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 65, 36, 43, 38, 55, 56, 52, 53, 57, 48, 85, 71, 34, 30, 61, 54],
        },
        "umpires": {
            "HP": "Kerwin Danley",
            "1B": "Mike Estabrook",
            "2B": "Chad Fairchild",
            "3B": "Chris Guccione",
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
# Pitching: NYY #19 Masahiro Tanaka
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b s")
t1.hit(2)
t1.advance(3, "16 G3-1")
t1.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t1.new_ab()
t1.pitch_list("b f f")
t1.out("G3-1")

# 3. BOS #28 J.D. Martinez (50 - X - X)
t1.new_ab()
t1.pitch_list("f b b b s")
t1.hit(1, rbis=1)
t1.error(2)
t1.advance(2, "2 SB")
t1.advance(3, "2 E2")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t1.new_ab()
t1.pitch_list("c b b c 1 1 f 1 f d s")
t1.out("K")

# 5. BOS #12 Brock Holt (28 - X - X)
t1.new_ab()
t1.pitch_list("b c s f f f d s")
t1.out("K")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. NYY #26 Andrew McCutchen (X - X - X)
b1.new_ab()
b1.pitch_list("b c b c b b")
b1.reach("BB")
b1.thrown_out(2, "31 CS", 2, 57)

# 2. NYY #99 Aaron Judge (X - X - 26)
b1.new_ab()
b1.pitch_list("f b c b b s")
b1.out("K")

# 3. NYY #31 Aaron Hicks (X - X - 26)
b1.new_ab()
b1.pitch_list("c d b f b f")
b1.hit(2)

# 4. NYY #27 Giancarlo Stanton (X - 31 - X)
b1.new_ab()
b1.pitch_list("b f b b f b")
b1.reach("BB")

# 5. NYY #18 Didi Gregorius (X - 31 - 27)
b1.new_ab()
b1.pitch_list("s b f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #19 Masahiro Tanaka
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f b f f")
t2.hit(1)
t2.advance(2, "23 1B")
t2.advance(3, "19 G3")
t2.advance(4, "50 1B")

# 7. BOS #23 Blake Swihart (X - X - 11)
t2.new_ab()
t2.hit(1)
t2.advance(2, "19 G3")
t2.advance(4, "50 1B")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 23)
t2.new_ab()
t2.out("G3")

# 9. BOS #7  Christian Vázquez (11 - 23 - X)
t2.new_ab()
t2.pitch_list("b c c s")
t2.out("K")

# 1. BOS #50 Mookie Betts (11 - 23 - X)
t2.new_ab()
t2.pitch_list("f f")
t2.hit(1, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t2.new_ab()
t2.pitch_list("1 b f b 1 c")
t2.out("G1-3")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 6. NYY #41 Miguel Andujar (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 7. NYY #24 Gary Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(4, "45 HR")

# 8. NYY #45 Luke Voit (X - X - 24)
b2.new_ab()
b2.pitch_list("b")
b2.hit(4, rbis=2)

# 9. NYY #25 Gleyber Torres (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c")
b2.hit(1)

# 2. NYY #99 Aaron Judge (X - X - 26)
b2.new_ab()
b2.pitch_list("b f b c b")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #19 Masahiro Tanaka
t3 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b b s")
t3.out("G5-3")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.out("G6-3")

# 5. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(4)

# 6. BOS #11 Rafael Devers (X - X - X)
t3.new_ab()
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 3. NYY #31 Aaron Hicks (X - X - X)
b3.new_ab()
b3.pitch_list("c s b s")
b3.out("K")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b3.new_ab()
b3.pitch_list("c b b c f f b b")
b3.reach("BB")
b3.advance(2, "18 1B")

# 5. NYY #18 Didi Gregorius (X - X - 27)
b3.new_ab()
b3.hit(1)

# 6. NYY #41 Miguel Andujar (X - 27 - 18)
b3.new_ab()
b3.pitch_list("d b f b")
b3.out("F7")

# 7. NYY #24 Gary Sánchez (X - 27 - 18)
b3.new_ab()
b3.pitch_list("c f t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #19 Masahiro Tanaka
t4 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
t4.new_ab()
t4.pitch_list("c s")
t4.out("G3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
t4.new_ab()
t4.pitch_list("c s f b")
t4.out("F8")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 8. NYY #45 Luke Voit (X - X - X)
b4.new_ab()
b4.pitch_list("s b f")
b4.out("L7")

# 9. NYY #25 Gleyber Torres (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F8")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b b")
b4.reach("BB")
b4.advance(2, "99 BB")
b4.advance(3, "31 BB")
b4.advance(4, "27 HR")

# 2. NYY #99 Aaron Judge (X - X - 26)
b4.new_ab()
b4.pitch_list("s f b f b b f f f b")
b4.reach("BB")
b4.advance(2, "31 BB")
b4.advance(4, "27 HR")

# 3. NYY #31 Aaron Hicks (X - 26 - 99)
b4.new_ab()
b4.pitch_list("c b c b b b")
b4.reach("BB")
b4.advance(4, "27 HR")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
b4.pitching_substitution(37)

# 4. NYY #27 Giancarlo Stanton (26 - 99 - 31)
b4.new_ab()
b4.pitch_list("c")
b4.hit(4, rbis=4)

# 5. NYY #18 Didi Gregorius (X - X - X)
b4.new_ab()
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #19 Masahiro Tanaka
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c b c b f")
t5.hit(2)
t5.advance(3, "16 1B")
t5.advance(4, "28 DP6-4-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.thrown_out(2, "28 DP6-4-3", 1, 30)

# Pitching change (NYY): #30 David Robertson replaces #19 Masahiro Tanaka
t5.pitching_substitution(30)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
t5.new_ab()
t5.pitch_list("f b d f f f")
t5.out("DP6-4-3")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #35 Steven Wright
b5 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #37 Heath Hembree
b5.pitching_substitution(35)

# 6. NYY #41 Miguel Andujar (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G4-3")

# 7. NYY #24 Gary Sánchez (X - X - X)
b5.new_ab()
b5.pitch_list("b c b c f b s")
b5.out("K")

# 8. NYY #45 Luke Voit (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("L4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #57 Chad Green
t6 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #30 David Robertson
t6.pitching_substitution(57)

# 5. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c f b s")
t6.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b b f f t")
t6.out("KT")

# 7. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c c s")
t6.out("K")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# 9. NYY #25 Gleyber Torres (X - X - X)
b6.new_ab()
b6.pitch_list("c s s")
b6.out("K")

# 1. NYY #26 Andrew McCutchen (X - X - X)
b6.new_ab()
b6.pitch_list("c b f")
b6.out("G5-3")

# 2. NYY #99 Aaron Judge (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #57 Chad Green
t7 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.hit(4)

# 9. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b c f f")
t7.hit(1)
t7.advance(3, "16 2B")
# Offensive change (BOS): Pinch-runner #30 Tzu-Wei Lin replaces #7 Christian Vázquez
t7.offensive_substitution(9, 30, "PR")
t7.atbase("PR")
t7.advance(4, "2 SF8")

# Pitching change (NYY): #68 Dellin Betances replaces #57 Chad Green
t7.pitching_substitution(68)

# 1. BOS #50 Mookie Betts (X - X - 7)
t7.new_ab()
t7.pitch_list("c b s c")
t7.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - 7)
t7.new_ab()
t7.pitch_list("b")
t7.hit(2)
t7.error(8)
t7.advance("U", "2 E8")

# 3. BOS #28 J.D. Martinez (7 - 16 - X)
t7.new_ab()
t7.pitch_list("v v v v")
t7.reach("IBB")
t7.advance(3, "2 E8")

# 4. BOS #2  Xander Bogaerts (7 - 16 - 28)
t7.new_ab()
t7.pitch_list("s f f b")
t7.out("SF8", rbis=1)

# 5. BOS #12 Brock Holt (28 - X - X)
t7.new_ab()
t7.pitch_list("f c b b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #35 Steven Wright
b7 = game.new_inning()

# Defensive change (BOS): #3 Sandy León replaces #30 Tzu-Wei Lin (PR), playing C, batting 9th
b7.defensive_substitution(9, 3, "2")

# 3. NYY #31 Aaron Hicks (X - X - X)
b7.new_ab()
b7.pitch_list("b c s f b f")
b7.out("P3")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 5. NYY #18 Didi Gregorius (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)

# 6. NYY #41 Miguel Andujar (X - X - 18)
b7.new_ab()
b7.pitch_list("s")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #54 Aroldis Chapman
t8 = game.new_inning()

# Pitching change (NYY): #54 Aroldis Chapman replaces #68 Dellin Betances
t8.pitching_substitution(54)

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(2, "19 BB")
t8.advance(4, "50 HR")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #23 Blake Swihart, batting 7th
t8.offensive_substitution(7, 25, "PH")

# 7. BOS #25 Steve Pearce (X - X - 11)
t8.new_ab()
t8.pitch_list("c b f f b f b f f")
t8.out("L7")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 11)
t8.new_ab()
t8.pitch_list("b b 1 s b 1 b")
t8.reach("BB")
t8.advance(4, "50 HR")

# 9. BOS #3  Sandy León (X - 11 - 19)
t8.new_ab()
t8.pitch_list("b b c s s")
t8.out("K")

# 1. BOS #50 Mookie Betts (X - 11 - 19)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(4, rbis=3)

# Pitching change (NYY): #56 Jonathan Holder replaces #54 Aroldis Chapman
t8.pitching_substitution(56)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("1 b")
t8.out("F9")


# Bot 8th
# Pitching: BOS #70 Ryan Brasier
b8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #35 Steven Wright
b8.pitching_substitution(70)

# Defensive change (BOS): #18 Mitch Moreland replaces #25 Steve Pearce (PH), playing 1B, batting 7th
b8.defensive_substitution(7, 18, "3")

# 7. NYY #24 Gary Sánchez (X - X - X)
b8.new_ab()
b8.pitch_list("c f")
b8.out("F7")

# 8. NYY #45 Luke Voit (X - X - X)
b8.new_ab()
b8.pitch_list("f b b s s")
b8.out("K")

# 9. NYY #25 Gleyber Torres (X - X - X)
b8.new_ab()
b8.pitch_list("c b b f")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #67 A.J. Cole
t9 = game.new_inning()

# Pitching change (NYY): #67 A.J. Cole replaces #56 Jonathan Holder
t9.pitching_substitution(67)

# 4. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.out("F7")

# Pitching change (NYY): #71 Stephen Tarpley replaces #67 A.J. Cole
t9.pitching_substitution(71)

# 5. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b b")
t9.reach("BB")

# 6. BOS #11 Rafael Devers (X - X - 12)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# 7. BOS #18 Mitch Moreland (X - X - 12)
t9.new_ab()
t9.pitch_list("c s f f c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #70 Ryan Brasier
b9.pitching_substitution(46)

# 1. NYY #26 Andrew McCutchen (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(3)

# 2. NYY #99 Aaron Judge (26 - X - X)
b9.new_ab()
b9.pitch_list("f d c b s")
b9.out("K")

# 3. NYY #31 Aaron Hicks (26 - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("(F)P5")

# 4. NYY #27 Giancarlo Stanton (26 - X - X)
b9.new_ab()
b9.pitch_list("b s b s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #35 Steven Wright
game.winning_pitcher(35, is_away_team=True)

# Loser team: NYY
# LP: NYY #57 Chad Green
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
