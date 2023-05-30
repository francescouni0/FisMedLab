#ifndef COMMON_H
#define COMMON_H

#include <cstdint>
#include <tbb/tbb.h>

class gamma_interaction{
    //uint32_t event_id;
    float event_id;
    float step_nr;
    float x;
    float y;
    float z;
    float enDiff;
    float proc_type;
    float time;
    
public:
    gamma_interaction(float e, float s_n, float x_p, float y_p,  float z_p, float e_d, float p_t, float t)
    {
        event_id=e;
        step_nr = s_n;
        x = x_p;
        y = y_p;
        z = z_p;
        enDiff = e_d;
        proc_type = p_t;
        time = t;
    }
};

extern tbb::concurrent_vector<gamma_interaction> gamma_interaction_vector;


// class photonTrack{
//     //uint32_t event_id;
//     float track_id;
//     float x;
//     float y;
//     float z;
//     
// public:
//     photonTrack(float t_p, float x_p, float y_p, float z_p)
//     {
//         track_id = t_p;
//         x = x_p;
//         y = y_p;
//         z = z_p;
//     }
// };
// 
// extern tbb::concurrent_vector<photonTrack> photonTrack_vector;
// 
class detection{
    //uint32_t event_id;
    float event_id;
    float energy;
    float time;
    float x;
    float y;
    
public:
    detection(float e, float en, float t, float x_p, float y_p)
    {
        event_id=e;
        energy=en;
        time = t;
        x = x_p;
        y = y_p;
    }
};

extern tbb::concurrent_vector<detection> detection_vector1;
extern tbb::concurrent_vector<detection> detection_vector2;
extern tbb::concurrent_vector<detection> detection_vector3;
extern tbb::concurrent_vector<detection> detection_vector4;



#endif
