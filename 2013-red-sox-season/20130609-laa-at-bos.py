import os
from baseball_scorecard.baseball_scorecard import Scorecard

# LAA @ BOS, 2013-06-09
# https://www.baseball-reference.com/boxes/BOS/BOS201306090.shtml
# https://www.mlb.com/gameday/angels-vs-red-sox/2013/06/09/347679/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-06-09 13:42-17:15",
        "at": "Fenway Park, Boston, MA",
        "att": "37,054",
        "temp": "76F, Sunny",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "Los Angeles Angels",
            "starter": 55,
            "roster": {
                # Lineup
                27: "Mike Trout",
                32: "Josh Hamilton",
                5: "Albert Pujols",
                44: "Mark Trumbo",
                47: "Howie Kendrick",
                6: "Alberto Callaspo",
                2: "Erick Aybar",
                17: "Chris Iannetta",
                39: "JB Shuck",
                # Starting pitcher
                55: "Joe Blanton",
                # Bench
                8: "Chris Nelson",
                16: "Hank Conger",
                20: "Brendan Harris",
                10: "Brad Hawpe",
                # Bullpen
                33: "C.J. Wilson",
                49: "Ernesto Frieri",
                40: "Kevin Jepsen",
                58: "Michael Kohn",
                37: "Scott Downs",
                57: "Jerome Williams",
                48: "Tommy Hanson",
                36: "Jered Weaver",
                59: "Robert Coello",
                60: "Jason Vargas",
            },
            "lefties": [33, 37, 60],
            "lineup": [
                [27, "8"],
                [32, "9"],
                [5, "0"],
                [44, "3"],
                [47, "4"],
                [6, "5"],
                [2, "6"],
                [17, "2"],
                [39, "7"],
            ],
            "bench": [
                [8, "3B"],
                [16, "C"],
                [20, "SS"],
                [10, "RF"],
            ],
            "bullpen": [33, 49, 40, 58, 37, 57, 48, 36, 59, 60],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                7: "Stephen Drew",
                10: "Jose Iglesias",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                3: "David Ross",
                18: "Shane Victorino",
                23: "Pedro Ciriaco",
                5: "Jonny Gomes",
                # Bullpen
                40: "Andrew Bailey",
                41: "John Lackey",
                56: "Franklin Morales",
                30: "Andrew Miller",
                32: "Craig Breslow",
                19: "Koji Uehara",
                31: "Jon Lester",
                59: "Clayton Mortensen",
                36: "Junichi Tazawa",
                22: "Felix Doubront",
            },
            "lefties": [56, 30, 32, 31, 22],
            "lineup": [
                [2, "8"],
                [29, "9"],
                [15, "4"],
                [34, "0"],
                [12, "3"],
                [39, "2"],
                [37, "7"],
                [7, "6"],
                [10, "5"],
            ],
            "bench": [
                [3, "C"],
                [18, "CF"],
                [23, "3B"],
                [5, "LF"],
            ],
            "bullpen": [40, 41, 56, 30, 32, 19, 31, 59, 36, 22],
        },
        "umpires": {
            "HP": "Marty Foster",
            "1B": "Wally Bell",
            "2B": "Marvin Hudson",
            "3B": "Tim McClelland",
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
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. LAA #27 Mike Trout (X - X - X)
t1.new_ab()
t1.pitch_list("b b f f b c")
t1.out("!K")

# 2. LAA #32 Josh Hamilton (X - X - X)
t1.new_ab()
t1.pitch_list("b f b s")
t1.out("G6-3")

# 3. LAA #5  Albert Pujols (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.hit(4)

# 4. LAA #44 Mark Trumbo (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b s")
t1.hit(1)

# 5. LAA #47 Howie Kendrick (X - X - 44)
t1.new_ab()
t1.pitch_list("c f b s")
t1.out("K")


# Bot 1st
# Pitching: LAA #55 Joe Blanton
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L7")

# 2. BOS #29 Daniel Nava (X - X - X)
b1.new_ab()
b1.pitch_list("b b c c f b")
b1.out("L8")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c b")
t2.reach("BB")
t2.thrown_out(2, "2 DP4-6-3", 1, 46)

# 7. LAA #2  Erick Aybar (X - X - 6)
t2.new_ab()
t2.pitch_list("1 c b")
t2.out("DP4-6-3")

# 8. LAA #17 Chris Iannetta (X - X - X)
t2.new_ab()
t2.pitch_list("s c b b s")
t2.out("K")


# Bot 2nd
# Pitching: LAA #55 Joe Blanton
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b f f")
b2.hit(1)
b2.advance(2, "37 BB")

# 5. BOS #12 Mike Napoli (X - X - 34)
b2.new_ab()
b2.pitch_list("f c s")
b2.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 34)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 7. BOS #37 Mike Carp (X - X - 34)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 8. BOS #7  Stephen Drew (X - 34 - 37)
b2.new_ab(is_risp=True)
b2.out("(F)P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 9. LAA #39 JB Shuck (X - X - X)
t3.new_ab()
t3.pitch_list("b b c")
t3.hit(2)
t3.advance(3, "44 WP")

# 1. LAA #27 Mike Trout (X - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c f")
t3.out("G1-3")

# 2. LAA #32 Josh Hamilton (X - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("s s d")
t3.out("L9")

# 3. LAA #5  Albert Pujols (X - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f")
t3.reach("HBP")
t3.advance(2, "44 BB")

# 4. LAA #44 Mark Trumbo (X - 39 - 5)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b b")
t3.wp()
t3.reach("BB")
t3.thrown_out(2, "47 FC6-4", 3, 46)

# 5. LAA #47 Howie Kendrick (39 - 5 - 44)
t3.new_ab(is_risp=True)
t3.pitch_list("s b")
t3.reach("FC6-4")


# Bot 3rd
# Pitching: LAA #55 Joe Blanton
b3 = game.new_inning()

# 9. BOS #10 Jose Iglesias (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.hit(1)
b3.thrown_out(2, "2 FC3-6", 1, 55)

# 1. BOS #2  Jacoby Ellsbury (X - X - 10)
b3.new_ab()
b3.pitch_list("b f l")
b3.reach("FC3-6")
b3.advance(2, "29 SB")
b3.advance(4, "29 1B")

# 2. BOS #29 Daniel Nava (X - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("d c 1 1 c f d")
b3.hit(1, rbis=1)
b3.advance(2, "15 1B")
b3.advance(4, "34 HR")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
b3.new_ab()
b3.pitch_list("c b b 1")
b3.hit(1)
b3.advance(4, "34 HR")

# 4. BOS #34 David Ortiz (X - 29 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("b f")
b3.hit(4, rbis=3)

# 5. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("b c t c")
b3.out("!K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
t4.new_ab()
t4.pitch_list("b b c")
t4.hit(4)

# 7. LAA #2  Erick Aybar (X - X - X)
t4.new_ab()
t4.pitch_list("c l")
t4.out("L7")

# 8. LAA #17 Chris Iannetta (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b s f f")
t4.out("P4")

# 9. LAA #39 JB Shuck (X - X - X)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("P6")


# Bot 4th
# Pitching: LAA #55 Joe Blanton
b4 = game.new_inning()

# 7. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c c b")
b4.error(5)
b4.reach("E5")
b4.advance(3, "10 WP")
b4.advance("U", "2 3B")

# 8. BOS #7  Stephen Drew (X - X - 37)
b4.new_ab()
b4.pitch_list("b c 1 s b s")
b4.out("K")

# 9. BOS #10 Jose Iglesias (X - X - 37)
b4.new_ab(is_risp=True)
b4.pitch_list("1 c l 1 f b b b")
b4.wp()
b4.out("(F)P3")

# 1. BOS #2  Jacoby Ellsbury (37 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b d c f b")
b4.hit(3, rbis=1)

# 2. BOS #29 Daniel Nava (2 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 1. LAA #27 Mike Trout (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.hit(2)
t5.advance(4, "44 1B")

# 2. LAA #32 Josh Hamilton (X - 27 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s s d c")
t5.out("!K")

# 3. LAA #5  Albert Pujols (X - 27 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("f c b b")
t5.out("F8")

# 4. LAA #44 Mark Trumbo (X - 27 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s s")
t5.hit(1, rbis=1)
t5.thrown_out(2, "47 FC4-6", 3, 46)

# 5. LAA #47 Howie Kendrick (X - X - 44)
t5.new_ab()
t5.pitch_list("c")
t5.reach("FC4-6")


# Bot 5th
# Pitching: LAA #55 Joe Blanton
b5 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f b f")
b5.out("P4")

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c s c")
b5.out("!K")

# 5. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("s b b s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 6. LAA #6  Alberto Callaspo (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f s")
t6.out("K")

# 7. LAA #2  Erick Aybar (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b")
t6.out("L7")

# 8. LAA #17 Chris Iannetta (X - X - X)
t6.new_ab()
t6.pitch_list("b s f f s")
t6.out("K")


# Bot 6th
# Pitching: LAA #55 Joe Blanton
b6 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.hit(4)

# 7. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.hit(4)

# Pitching change (LAA): #58 Michael Kohn replaces #55 Joe Blanton
b6.pitching_substitution(58)

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b f b")
b6.error(4)
b6.reach("E4")
b6.advance(2, "10 PB")

# 9. BOS #10 Jose Iglesias (X - X - 7)
b6.new_ab(is_risp=True)
b6.pitch_list("f 1 b s f f f d f")
b6.pb()
b6.out("F9")

# 1. BOS #2  Jacoby Ellsbury (X - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c f d f")
b6.out("F9")

# 2. BOS #29 Daniel Nava (X - 7 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b c b c f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Craig Breslow
t7 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #46 Ryan Dempster
t7.pitching_substitution(32)

# 9. LAA #39 JB Shuck (X - X - X)
t7.new_ab()
t7.out("(F)B5")

# 1. LAA #27 Mike Trout (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.hit(2)
t7.advance(3, "32 G6-3")

# 2. LAA #32 Josh Hamilton (X - 27 - X)
t7.new_ab(is_risp=True)
t7.out("G6-3")

# 3. LAA #5  Albert Pujols (27 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c f")
t7.out("(F)P3")


# Bot 7th
# Pitching: LAA #59 Robert Coello
b7 = game.new_inning()

# Pitching change (LAA): #59 Robert Coello replaces #58 Michael Kohn
b7.pitching_substitution(59)

# 3. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("F7")

# 4. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.advance(2, "12 BB")
b7.advance(4, "39 HR")

# 5. BOS #12 Mike Napoli (X - X - 34)
b7.new_ab()
b7.pitch_list("b b b c s b")
b7.reach("BB")
b7.advance(4, "39 HR")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.hit(4, rbis=3)

# 7. BOS #37 Mike Carp (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f")
b7.out("F8")

# 8. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.pitch_list("c c f")
b7.hit(1)
b7.advance(3, "10 2B")

# 9. BOS #10 Jose Iglesias (X - X - 7)
b7.new_ab()
b7.hit(2)

# 1. BOS #2  Jacoby Ellsbury (7 - 10 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f b f b b b")
b7.reach("BB")

# Pitching change (LAA): #37 Scott Downs replaces #59 Robert Coello
b7.pitching_substitution(37)

# 2. BOS #29 Daniel Nava (7 - 10 - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("f b b c")
b7.out("L7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #19 Koji Uehara
t8 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t8.pitching_substitution(19)

# Defensive change (BOS): #23 Pedro Ciriaco replaces #15 Dustin Pedroia (2B), playing 3B, batting 3rd
t8.defensive_substitution(3, 23, "5")

# Defensive switch (BOS): #10 Jose Iglesias moves to 2B
t8.defensive_switch(10, "4")

# 4. LAA #44 Mark Trumbo (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f")
t8.out("G6-3")

# 5. LAA #47 Howie Kendrick (X - X - X)
t8.new_ab()
t8.reach("HBP")
t8.thrown_out(2, "6 FC3-6", 2, 19)

# 6. LAA #6  Alberto Callaspo (X - X - 47)
t8.new_ab()
t8.pitch_list("b f b s f")
t8.reach("FC3-6")
t8.advance(2, "2 BB")
t8.advance(3, "17 BB")
t8.advance(4, "39 1B")

# 7. LAA #2  Erick Aybar (X - X - 6)
t8.new_ab()
t8.pitch_list("b b c c b b")
t8.reach("BB")
t8.advance(2, "17 BB")
t8.advance(4, "39 1B")

# 8. LAA #17 Chris Iannetta (X - 6 - 2)
t8.new_ab(is_risp=True)
t8.pitch_list("s c d f f b f b b")
t8.reach("BB")
t8.advance(2, "39 1B")
t8.advance(3, "27 1B")

# 9. LAA #39 JB Shuck (6 - 2 - 17)
t8.new_ab(is_risp=True)
t8.pitch_list("b c f")
t8.hit(1, rbis=2)
t8.advance(2, "27 1B")
t8.thrown_out(3, "27 9-6", 3, 30)

# Pitching change (BOS): #30 Andrew Miller replaces #19 Koji Uehara
t8.pitching_substitution(30)

# 1. LAA #27 Mike Trout (X - 17 - 39)
t8.new_ab(is_risp=True)
t8.pitch_list("c f b b")
t8.hit(1)


# Bot 8th
# Pitching: LAA #40 Kevin Jepsen
b8 = game.new_inning()

# Pitching change (LAA): #40 Kevin Jepsen replaces #37 Scott Downs
b8.pitching_substitution(40)

# 3. BOS #23 Pedro Ciriaco (X - X - X)
b8.new_ab()
b8.pitch_list("f f")
b8.out("G3")

# 4. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G6-3")

# 5. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b f b f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #40 Andrew Bailey
t9 = game.new_inning()

# Pitching change (BOS): #40 Andrew Bailey replaces #30 Andrew Miller
t9.pitching_substitution(40)

# 2. LAA #32 Josh Hamilton (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b f f s")
t9.out("K")

# 3. LAA #5  Albert Pujols (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("(F)P3")

# 4. LAA #44 Mark Trumbo (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c f f f d")
t9.reach("BB")

# 5. LAA #47 Howie Kendrick (X - X - 44)
t9.new_ab()
t9.pitch_list("c b s f f d c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)

# Loser team: LAA
# LP: LAA #55 Joe Blanton
game.losing_pitcher(55, is_away_team=True)

# print(game)
game.generate_scorecard()
