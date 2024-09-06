import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-08-02
# https://www.baseball-reference.com/boxes/BOS/BOS201808020.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/08/02/531045/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-02 19:10-22:35",
        "at": "Fenway Park, Boston, MA",
        "att": "37,317",
        "temp": "87F, Partly Cloudy",
        "wind": "15mph, Out To LF",
        "away": {
            "team": "New York Yankees",
            "starter": 52,
            "roster": {
                # Lineup
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                25: "Gleyber Torres",
                41: "Miguel Andujar",
                33: "Greg Bird",
                45: "Luke Voit",
                28: "Austin Romine",
                11: "Brett Gardner",
                # Starting pitcher
                52: "CC Sabathia",
                # Bench
                66: "Kyle Higashioka",
                38: "Shane Robinson",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                36: "Lance Lynn",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                53: "Zack Britton",
                19: "Masahiro Tanaka",
                57: "Chad Green",
                85: "Luis Cessa",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 54],
            "lineup": [
                [31, "8"],
                [27, "9"],
                [18, "6"],
                [25, "4"],
                [41, "5"],
                [33, "3"],
                [45, "0"],
                [28, "2"],
                [11, "7"],
            ],
            "bench": [
                [66, "C"],
                [38, "CF"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 36, 55, 56, 53, 19, 57, 85, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [61, 31, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [25, "3"],
                [28, "0"],
                [5, "4"],
                [36, "5"],
                [23, "2"],
                [12, "6"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [2, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Dan Bellino",
            "1B": "Adam Hamari",
            "2B": "Phil Cuzzi",
            "3B": "Chris Conroy",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
t1.new_ab()
t1.pitch_list("b f s b f")
t1.error(6)
t1.reach("E6")
t1.advance(2, "27 1B")
t1.advance("U", "18 HR")

# 2. NYY #27 Giancarlo Stanton (X - X - 31)
t1.new_ab()
t1.hit(1)
t1.advance(4, "18 HR")

# 3. NYY #18 Didi Gregorius (X - 31 - 27)
t1.new_ab()
t1.pitch_list("b b")
t1.hit(4, rbis=3)

# 4. NYY #25 Gleyber Torres (X - X - X)
t1.new_ab()
t1.pitch_list("b c c s")
t1.out("K")

# 5. NYY #41 Miguel Andujar (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("P6")

# 6. NYY #33 Greg Bird (X - X - X)
t1.new_ab()
t1.pitch_list("b b c f f")
t1.hit(1)

# 7. NYY #45 Luke Voit (X - X - 33)
t1.new_ab()
t1.pitch_list("c b")
t1.out("L9")


# Bot 1st
# Pitching: NYY #52 CC Sabathia
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f b f b")
b1.reach("BB")
b1.advance(2, "25 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("1 b c f")
b1.out("L7")

# 3. BOS #25 Steve Pearce (X - X - 50)
b1.new_ab()
b1.pitch_list("b f s")
b1.out("F8")

# 4. BOS #28 J.D. Martinez (X - 50 - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 8. NYY #28 Austin Romine (X - X - X)
t2.new_ab()
t2.pitch_list("c f b f b f s")
t2.out("K")

# 9. NYY #11 Brett Gardner (X - X - X)
t2.new_ab()
t2.pitch_list("c b c b c")
t2.out("!K")

# 1. NYY #31 Aaron Hicks (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(4, rbis=1)

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b s s")
t2.out("K")


# Bot 2nd
# Pitching: NYY #52 CC Sabathia
b2 = game.new_inning()

# 5. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f b f f f b")
b2.hit(1)
b2.advance(2, "36 1B")
b2.advance(3, "12 BB")
b2.advance(4, "50 BB")

# 6. BOS #36 Eduardo Núñez (X - X - 5)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.advance(2, "12 BB")
b2.advance(3, "50 BB")

# 7. BOS #23 Blake Swihart (X - 5 - 36)
b2.new_ab()
b2.pitch_list("c f d s")
b2.out("K")

# 8. BOS #12 Brock Holt (X - 5 - 36)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(2, "50 BB")

# 9. BOS #19 Jackie Bradley Jr. (5 - 36 - 12)
b2.new_ab()
b2.pitch_list("f f d c")
b2.out("!K")

# 1. BOS #50 Mookie Betts (5 - 36 - 12)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB", rbis=1)

# 2. BOS #16 Andrew Benintendi (36 - 12 - 50)
b2.new_ab()
b2.pitch_list("b f f d d")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 3. NYY #18 Didi Gregorius (X - X - X)
t3.new_ab()
t3.pitch_list("c f f b b f f c")
t3.out("!K")

# 4. NYY #25 Gleyber Torres (X - X - X)
t3.new_ab()
t3.pitch_list("b b f b b")
t3.reach("BB")

# 5. NYY #41 Miguel Andujar (X - X - 25)
t3.new_ab()
t3.pitch_list("b")
t3.out("L6")

# 6. NYY #33 Greg Bird (X - X - 25)
t3.new_ab()
t3.pitch_list("s 1 l s")
t3.out("K")


# Bot 3rd
# Pitching: NYY #52 CC Sabathia
b3 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("b c f")
b3.hit(4, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c c f b")
b3.reach("BB")
b3.advance(2, "36 SB")
b3.thrown_out(3, "36 FC6-4", 2, 52)

# 5. BOS #5  Ian Kinsler (X - X - 28)
b3.new_ab()
b3.out("F9")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
b3.new_ab()
b3.pitch_list("b c f f")
b3.reach("FC6-4")
b3.advance(3, "23 E1")

# 7. BOS #23 Blake Swihart (X - X - 36)
b3.new_ab()
b3.pitch_list("b")
b3.error(1)
b3.reach("E1", end_base=2)

# 8. BOS #12 Brock Holt (36 - 23 - X)
b3.new_ab()
b3.pitch_list("b b c")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 7. NYY #45 Luke Voit (X - X - X)
t4.new_ab()
t4.pitch_list("b s b b")
t4.out("P4")

# 8. NYY #28 Austin Romine (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(2)

# 9. NYY #11 Brett Gardner (X - 28 - X)
t4.new_ab()
t4.pitch_list("b b c f c")
t4.out("!K")

# 1. NYY #31 Aaron Hicks (X - 28 - X)
t4.new_ab()
t4.pitch_list("b d c d b")
t4.reach("BB")

# 2. NYY #27 Giancarlo Stanton (X - 28 - 31)
t4.new_ab()
t4.pitch_list("b b s s d c")
t4.out("!K")


# Bot 4th
# Pitching: NYY #56 Jonathan Holder
b4 = game.new_inning()

# Pitching change (NYY): #56 Jonathan Holder replaces #52 CC Sabathia
b4.pitching_substitution(56)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b b b c b")
b4.reach("BB")
b4.advance(3, "50 2B")
b4.advance(4, "16 FC1")

# 1. BOS #50 Mookie Betts (X - X - 19)
b4.new_ab()
b4.pitch_list("1 b")
b4.hit(2)
b4.advance(3, "16 FC1")
b4.advance(4, "25 HR")

# 2. BOS #16 Andrew Benintendi (19 - 50 - X)
b4.new_ab()
b4.pitch_list("c c b f")
b4.reach("FC1", rbis=1)
b4.advance(2, "25 SB")
b4.advance(4, "25 HR")

# 3. BOS #25 Steve Pearce (50 - X - 16)
b4.new_ab()
b4.pitch_list("s b 1 n d")
b4.hit(4, rbis=3)

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(2)
b4.advance(4, "5 1B")

# 5. BOS #5  Ian Kinsler (X - 28 - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1, rbis=1)
b4.advance(2, "36 SB")
b4.advance(4, "36 2B")

# 6. BOS #36 Eduardo Núñez (X - X - 5)
b4.new_ab()
b4.pitch_list("c 1 1 b l")
b4.hit(2, rbis=1)
b4.advance(4, "19 2B")

# Pitching change (NYY): #57 Chad Green replaces #56 Jonathan Holder
b4.pitching_substitution(57)

# 7. BOS #23 Blake Swihart (X - 36 - X)
b4.new_ab()
b4.pitch_list("c f s")
b4.out("K")

# 8. BOS #12 Brock Holt (X - 36 - X)
b4.new_ab()
b4.pitch_list("b f s")
b4.out("L9")

# 9. BOS #19 Jackie Bradley Jr. (X - 36 - X)
b4.new_ab()
b4.hit(2, rbis=1)
b4.advance(3, "50 1B")
b4.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.hit(1)
b4.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(1, rbis=1)
b4.thrown_out(2, "25 FC6-4", 3, 85)

# Pitching change (NYY): #85 Luis Cessa replaces #57 Chad Green
b4.pitching_substitution(85)

# 3. BOS #25 Steve Pearce (50 - X - 16)
b4.new_ab()
b4.pitch_list("d 1")
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 3. NYY #18 Didi Gregorius (X - X - X)
t5.new_ab()
t5.pitch_list("b f b f f")
t5.hit(4, rbis=1)

# 4. NYY #25 Gleyber Torres (X - X - X)
t5.new_ab()
t5.pitch_list("f f s")
t5.out("K")

# 5. NYY #41 Miguel Andujar (X - X - X)
t5.new_ab()
t5.pitch_list("b c s c")
t5.out("!K")

# 6. NYY #33 Greg Bird (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")


# Bot 5th
# Pitching: NYY #85 Luis Cessa
b5 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.hit(2)
b5.advance(3, "5 WP")
b5.advance(4, "5 2B")

# 5. BOS #5  Ian Kinsler (X - 28 - X)
b5.new_ab()
b5.pitch_list("f b d f f")
b5.wp()
b5.hit(2, rbis=1)

# 6. BOS #36 Eduardo Núñez (X - 5 - X)
b5.new_ab()
b5.out("P4")

# 7. BOS #23 Blake Swihart (X - 5 - X)
b5.new_ab()
b5.out("(F)P5")

# 8. BOS #12 Brock Holt (X - 5 - X)
b5.new_ab()
b5.pitch_list("c c d")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Brandon Workman
t6 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #61 Brian Johnson
t6.pitching_substitution(44)

# Defensive change (BOS): #3 Sandy León replaces #23 Blake Swihart (C), playing C, batting 7th
t6.defensive_substitution(7, 3, "2")

# 7. NYY #45 Luke Voit (X - X - X)
t6.new_ab()
t6.out("G6-3")

# 8. NYY #28 Austin Romine (X - X - X)
t6.new_ab()
t6.pitch_list("c c s")
t6.out("K")

# 9. NYY #11 Brett Gardner (X - X - X)
t6.new_ab()
t6.pitch_list("c c f f")
t6.out("G3-1")


# Bot 6th
# Pitching: NYY #85 Luis Cessa
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b b s c s")
b6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)
b6.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(2, rbis=1)
b6.advance(4, "25 HR")

# 3. BOS #25 Steve Pearce (X - 16 - X)
b6.new_ab()
b6.pitch_list("f s d")
b6.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.out("F8")

# 5. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Brandon Workman
t7 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c f")
t7.out("L4")

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t7.new_ab()
t7.pitch_list("b c f b b")
t7.hit(4, rbis=1)

# 3. NYY #18 Didi Gregorius (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3-1")

# 4. NYY #25 Gleyber Torres (X - X - X)
t7.new_ab()
t7.pitch_list("s c")
t7.out("G4-3")


# Bot 7th
# Pitching: NYY #85 Luis Cessa
b7 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.out("G4-3")

# 7. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("P6")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
t8.pitching_substitution(56)

# 5. NYY #41 Miguel Andujar (X - X - X)
t8.new_ab()
t8.pitch_list("f f")
t8.out("L7")

# 6. NYY #33 Greg Bird (X - X - X)
t8.new_ab()
t8.out("F7")

# 7. NYY #45 Luke Voit (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.out("L9")


# Bot 8th
# Pitching: NYY #85 Luis Cessa
b8 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.out("G4-1")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "16 1B")
b8.advance(3, "25 BB")
b8.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.pitch_list("f b f")
b8.hit(1)
b8.advance(2, "25 BB")
b8.advance(3, "28 1B")

# 3. BOS #25 Steve Pearce (X - 50 - 16)
b8.new_ab()
b8.pitch_list("d b b c b")
b8.reach("BB")
b8.advance(2, "28 1B")
b8.thrown_out(3, "5 DP6-4", 3, 53)

# Pitching change (NYY): #53 Zack Britton replaces #85 Luis Cessa
b8.pitching_substitution(53)

# 4. BOS #28 J.D. Martinez (50 - 16 - 25)
b8.new_ab()
b8.pitch_list("b c")
b8.hit(1, rbis=1)

# 5. BOS #5  Ian Kinsler (16 - 25 - 28)
b8.new_ab()
b8.pitch_list("b c")
b8.out("DP6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #70 Ryan Brasier
t9 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
t9.pitching_substitution(70)

# 8. NYY #28 Austin Romine (X - X - X)
t9.new_ab()
t9.pitch_list("f s f s")
t9.out("K")

# 9. NYY #11 Brett Gardner (X - X - X)
t9.new_ab()
t9.pitch_list("c s")
t9.hit(3)
t9.advance(4, "27 SF8")

# 1. NYY #31 Aaron Hicks (11 - X - X)
t9.new_ab()
t9.pitch_list("b b b c f b")
t9.reach("BB")
t9.advance(2, "27 DI")

# 2. NYY #27 Giancarlo Stanton (11 - X - 31)
t9.new_ab()
t9.pitch_list("b s f d f b")
t9.out("SF8", rbis=1)

# 3. NYY #18 Didi Gregorius (X - 31 - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("G6-3")

# Winning team: BOS
# WP: BOS #61 Brian Johnson
game.winning_pitcher(61)

# Loser team: NYY
# LP: NYY #56 Jonathan Holder
game.losing_pitcher(56, is_away_team=True)

# print(game)
game.generate_scorecard()
