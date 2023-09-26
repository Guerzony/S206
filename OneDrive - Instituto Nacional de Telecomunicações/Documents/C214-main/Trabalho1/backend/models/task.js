import mongoose, { Schema } from 'mongoose';

const taskSchema = new Schema({
    title: {
        type: String,
        required: true,
    },
    description : {
        type: String,
        required: true
    },
    status : {
        type: String,
        required: true
    }
    
},{versionKey: false});

export default mongoose.model('Task', taskSchema);