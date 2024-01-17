import {Link} from 'react-router-dom'

export function Navigation(){
    return(
        <div>
            <h1>
                <Link to="/tasks">Task App</Link>
            </h1>
            <Link to="/tasks-create"> Create Task</Link>

        </div>
    )
}