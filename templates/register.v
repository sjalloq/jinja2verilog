always@( {{clockedge}} {{clock}} or {{resetedge}} {{reset}} )
  if( {{resetpolarity}}{{reset}} )
    begin
       {{name}}_r <= {{resetval}};
    end
  else
    begin
       {{name}}_r <= {{name}}_nxt;
    end

   
